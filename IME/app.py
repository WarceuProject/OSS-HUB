import os
import io
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image, ImageStat, ImageFilter, ImageChops
import piexif

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024
app.config["UPLOAD_FOLDER"] = "uploads"

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def safe_div(n, d):
    return n / d if d else 0

def convert_gps(coord, ref):
    value = safe_div(coord[0][0], coord[0][1]) + \
            (safe_div(coord[1][0], coord[1][1]) / 60.0) + \
            (safe_div(coord[2][0], coord[2][1]) / 3600.0)
    if ref in [b'S', b'W', 'S', 'W']:
        value = -value
    return value

def check_letterbox(img):
    try:
        small = img.convert('L').resize((100, 100))
        w, h = small.size
        
        top = small.crop((0, 0, w, 15))
        bottom = small.crop((0, h-15, w, h))
        mid = small.crop((0, 15, w, h-15))
        
        st = ImageStat.Stat(top)
        sb = ImageStat.Stat(bottom)
        sm = ImageStat.Stat(mid)
        
        if st.stddev[0] < 8 and sb.stddev[0] < 8 and sm.stddev[0] > 15:
            return True
            
        left = small.crop((0, 0, 15, h))
        right = small.crop((w-15, 0, w, h))
        mid_v = small.crop((15, 0, w-15, h))
        
        sl = ImageStat.Stat(left)
        sr = ImageStat.Stat(right)
        sm_v = ImageStat.Stat(mid_v)
        
        if sl.stddev[0] < 8 and sr.stddev[0] < 8 and sm_v.stddev[0] > 15:
            return True
    except:
        pass
    return False

def get_quantization_info(img):
    info = {
        "luma_sum": 0,
        "chroma_sum": 0,
        "luma_table": [],
        "chroma_table": []
    }
    if hasattr(img, 'quantization') and img.quantization:
        try:
            if 0 in img.quantization:
                info["luma_table"] = img.quantization[0]
                info["luma_sum"] = sum(img.quantization[0])
            if 1 in img.quantization:
                info["chroma_table"] = img.quantization[1]
                info["chroma_sum"] = sum(img.quantization[1])
        except:
            pass
    return info

def analyze_pixels(img):
    try:
        gray = img.convert('L')
        edges = gray.filter(ImageFilter.FIND_EDGES)
        stat = ImageStat.Stat(edges)
        
        w, h = gray.size
        cx, cy = w // 2, h // 2
        box = max(100, min(w, h) // 4)
        center = gray.crop((cx - box // 2, cy - box // 2, cx + box // 2, cy + box // 2))
        center_edges = center.filter(ImageFilter.FIND_EDGES)
        c_stat = ImageStat.Stat(center_edges)

        ela_mean = 0.0
        ela_block_var = 0.0
        ela_block_max = 0.0
        
        if img.format in ['JPEG', 'WEBP', 'PNG']:
            buffer = io.BytesIO()
            img.convert('RGB').save(buffer, format='JPEG', quality=90)
            buffer.seek(0)
            recompressed = Image.open(buffer)
            ela = ImageChops.difference(img.convert('RGB'), recompressed).convert('L')
            ela_stat = ImageStat.Stat(ela)
            ela_mean = ela_stat.mean[0]
            
            small_ela = ela.resize((32, 32), Image.Resampling.BOX)
            small_stat = ImageStat.Stat(small_ela)
            ela_block_var = small_stat.var[0]
            ela_block_max = small_stat.extrema[0][1]
        
        return stat.var[0], c_stat.var[0], ela_mean, ela_block_var, ela_block_max
    except:
        return 0.0, 0.0, 0.0, 0.0, 0.0

def analyze_image(exif_dict, img, original_filename, filesize):
    features = {
        "camera_photo": False,
        "camera_photo_recaptured": False,
        "screen_capture": False,
        "edited": False,
        "local_tampering": False,
        "editor_reencoded": False,
        "ai_generated": False,
        "platform_reencoded": False
    }
    software_used = []
    origins = []
    notes = []
    has_exif = False
    has_camera_model = False
    is_screenshot_heuristics = False

    screenshot_keywords = ['screenshot', 'screen_shot', 'capture', 'screencap', 'screencast', 'prtsc', 'snap', 'ss-']
    editing_software = ['photoshop', 'lightroom', 'gimp', 'canva', 'snapseed', 'picsart', 'vsco', 'remini', 'faceapp', 'meitu', 'capcut', 'b612', 'beautyplus', 'illustrator', 'coreldraw', 'polarr', 'pixlr']
    social_platforms = ['instagram', 'facebook', 'twitter', 'tiktok', 'whatsapp', 'telegram', 'discord', 'line', 'wechat', 'reddit', 'messenger']
    ai_generators = ['midjourney', 'stable diffusion', 'dall-e', 'novelai', 'firefly', 'bing image creator', 'comfyui']
    screenshot_software = ['sharex', 'snipping tool', 'mac os x', 'gnome-screenshot', 'spectacle', 'android', 'screenshot']
    social_media_dimensions = [720, 800, 1024, 1080, 1280, 1350, 1600, 2048]

    filename_lower = original_filename.lower()
    if any(x in filename_lower for x in screenshot_keywords):
        is_screenshot_heuristics = True
        origins.append("screenshot_from_filename")
    if any(x in filename_lower for x in social_platforms):
        origins.append("social_media_from_filename")

    for key, value in img.info.items():
        if isinstance(value, bytes):
            try:
                value = value.decode('utf-8', 'ignore').lower()
            except:
                value = ""
        elif isinstance(value, str):
            value = value.lower()
        else:
            value = str(value).lower()
            
        key_lower = str(key).lower()

        if any(x in value for x in screenshot_keywords):
            is_screenshot_heuristics = True
            origins.append("screenshot_from_metadata")
        if any(x in value for x in ai_generators):
            features["ai_generated"] = True
            origins.append("ai_generated_from_metadata")
        if any(x in value for x in social_platforms):
            origins.append("social_media_from_metadata")
            
        if key_lower in ['software', 'processingsoftware', 'creator', 'description']:
            software_used.append(value)
            if any(x in value for x in screenshot_software):
                is_screenshot_heuristics = True

    if exif_dict:
        if "0th" in exif_dict and exif_dict["0th"]:
            has_exif = True
            make = exif_dict["0th"].get(piexif.ImageIFD.Make)
            model = exif_dict["0th"].get(piexif.ImageIFD.Model)
            software = exif_dict["0th"].get(piexif.ImageIFD.Software)
            
            if make or model:
                has_camera_model = True

            if software:
                try:
                    sw_str = software.decode('utf-8', 'ignore').lower()
                    software_used.append(sw_str)
                    if any(x in sw_str for x in editing_software):
                        features["edited"] = True
                    if any(x in sw_str for x in social_platforms):
                        origins.append("social_media_exif_tag")
                    if any(x in sw_str for x in screenshot_software):
                        is_screenshot_heuristics = True
                        origins.append("screenshot_from_exif")
                    if any(x in sw_str for x in ai_generators):
                        features["ai_generated"] = True
                        origins.append("ai_generated_from_exif")
                except:
                    pass

        if "Exif" in exif_dict and exif_dict["Exif"]:
            has_exif = True
            user_comment = exif_dict["Exif"].get(piexif.ExifIFD.UserComment)
            if user_comment:
                try:
                    uc_str = user_comment.decode('utf-8', 'ignore').lower()
                    if 'screenshot' in uc_str:
                        is_screenshot_heuristics = True
                        origins.append("screenshot_from_exif_comment")
                except:
                    pass

    try:
        icc = img.info.get('icc_profile', b'').lower()
        if b'cnrgb' in icc or b'facebook' in icc:
            origins.append("meta_icc_profile")
        if b'google' in icc:
            origins.append("google_icc_profile")
        if b'display p3' in icc and img.format == 'PNG' and not has_camera_model:
            is_screenshot_heuristics = True
            origins.append("ios_mac_screenshot_profile")
        if b'srgb iec61966-2.1' in icc and img.format == 'PNG' and not has_camera_model:
            origins.append("generic_srgb_png_possible_screenshot")
    except:
        pass

    is_letterboxed = check_letterbox(img)
    q_info = get_quantization_info(img)
    q_sum = q_info["luma_sum"]
    edge_var, center_edge_var, ela_mean, ela_block_var, ela_block_max = analyze_pixels(img)
    
    width, height = img.size
    max_dim = max(width, height)
    bpp = (filesize * 8) / (width * height) if (width * height) > 0 else 0

    pixel_data = {
        "quantization": q_info,
        "edge_variance": round(edge_var, 2),
        "center_edge_variance": round(center_edge_var, 2),
        "ela_mean": round(ela_mean, 2),
        "ela_macro_block_variance": round(ela_block_var, 2),
        "ela_macro_block_max": round(ela_block_max, 2)
    }

    if is_screenshot_heuristics or (img.format == 'PNG' and not has_exif):
        if is_letterboxed or (center_edge_var > 1500 and q_sum > 0):
            features["camera_photo_recaptured"] = True
            origins.append("screenshot_of_photo_detected_via_moire_or_letterbox")
        else:
            features["screen_capture"] = True
    elif not has_exif and img.format == 'JPEG':
        if is_letterboxed or center_edge_var > 2000:
            features["camera_photo_recaptured"] = True
            origins.append("recaptured_screen_detected_via_pixel_noise")

    if not has_exif and img.format in ['JPEG', 'WEBP'] and not is_screenshot_heuristics and not features["camera_photo_recaptured"] and not features["edited"] and not features["ai_generated"]:
        if max_dim > 1600 and (bpp < 0.8 or q_sum > 1000):
            features["editor_reencoded"] = True
            notes.append("High resolution retained but EXIF metadata removed.")
            notes.append("Aggressive JPEG quantization or low BPP detected, typical of manual export/web optimization.")
            if q_sum > 1000:
                notes.append(f"Very high quantization sum ({q_sum}) indicates manual software compression ('Save for Web').")
        else:
            features["platform_reencoded"] = True
            notes.append("All camera EXIF metadata is missing completely.")
            if max_dim in social_media_dimensions or (width == 720 and height == 1280):
                notes.append(f"Resolution ({width}x{height}) matches common social media compression scaling.")
            elif max_dim <= 1600:
                notes.append(f"Max dimension ({max_dim}px) is within typical messaging platform limits.")
            else:
                notes.append("Resolution does not match typical native camera sensor outputs.")
            if bpp < 1.5:
                notes.append(f"Low bits-per-pixel ratio ({bpp:.2f}) strongly indicates heavy platform re-compression.")
            if 300 < q_sum < 600:
                notes.append(f"JPEG quantization table sum ({q_sum}) matches standard social media web compression.")

    if ela_block_max > (ela_mean * 2.5) and ela_block_max > 15.0 and ela_block_var > 10.0:
        features["local_tampering"] = True
        features["edited"] = True
        notes.append(f"High localized ELA anomalies (max block: {round(ela_block_max, 2)}, variance: {round(ela_block_var, 2)}). Strong indicator of selective image tampering or object splicing.")
    elif ela_mean > 12.0 and not features["ai_generated"] and not is_screenshot_heuristics:
        features["edited"] = True
        notes.append(f"High Error Level Analysis mean ({round(ela_mean, 2)}) suggests image manipulation or multiple global re-saves.")

    if has_camera_model and not is_screenshot_heuristics and not features["ai_generated"] and not is_letterboxed and not features["edited"]:
        if center_edge_var > 2500 and q_sum > 0:
            features["camera_photo_recaptured"] = True
            notes.append(f"High frequency center pixel noise ({round(center_edge_var, 2)}) indicates Moiré pattern from screen recapture.")
        else:
            features["camera_photo"] = True
            notes.append("Contains original camera metadata and typical sensor characteristics.")

    if features["camera_photo_recaptured"]:
        features["screen_capture"] = False
        features["camera_photo"] = False
        notes.append("Detected letterboxing or Moiré patterns, indicating a photo of a photo/screen.")

    if q_sum > 800 and not features["editor_reencoded"]:
        notes.append(f"Extremely high JPEG quantization sum ({q_sum}), heavy compression detected.")
    elif q_sum > 0 and q_sum < 250 and features["camera_photo"]:
        notes.append(f"Low JPEG quantization sum ({q_sum}), matches high-quality native camera processing.")

    verdict = "unknown"
    confidence = 0.0

    if features["local_tampering"]:
        verdict = "tampered_spliced"
        confidence = 0.93
    elif features["ai_generated"]:
        verdict = "ai_generated"
        confidence = 0.95
    elif features["camera_photo_recaptured"]:
        verdict = "camera_photo_recaptured"
        confidence = 0.92
    elif features["screen_capture"]:
        verdict = "screen_capture"
        confidence = 0.90
    elif features["editor_reencoded"]:
        verdict = "editor_reencoded"
        confidence = 0.92
    elif features["edited"]:
        verdict = "edited"
        confidence = 0.85
    elif features["platform_reencoded"]:
        verdict = "platform_reencoded"
        confidence = 0.88
    elif features["camera_photo"]:
        verdict = "camera_photo"
        confidence = 0.94

    return {
        "verdict": verdict,
        "confidence": confidence,
        "notes": notes,
        "features": features,
        "pixel_analysis": pixel_data,
        "software_detected": list(set([s.strip() for s in software_used if s.strip()])),
        "detected_origins": list(set(origins))
    }

def process_image(filepath, original_filename):
    data = {}
    try:
        filesize = os.path.getsize(filepath)
        with Image.open(filepath) as img:
            data["format"] = img.format
            data["mode"] = img.mode
            data["width"] = img.width
            data["height"] = img.height
            data["filesize_bytes"] = filesize
            
            exif_raw = img.info.get('exif')
            exif_dict = None
            
            if exif_raw:
                try:
                    exif_dict = piexif.load(exif_raw)
                except:
                    pass
                    
            data["analysis"] = analyze_image(exif_dict, img, original_filename, filesize)
            
            if exif_dict:
                for ifd in ("0th", "Exif"):
                    for tag in exif_dict.get(ifd, {}):
                        try:
                            tag_name = piexif.TAGS[ifd][tag]["name"]
                            val = exif_dict[ifd][tag]
                            if isinstance(val, bytes):
                                val = val.decode('utf-8', 'ignore')
                            elif isinstance(val, tuple):
                                val = str(val)
                            data[tag_name] = val
                        except:
                            continue
                            
                gps = exif_dict.get("GPS", {})
                if gps:
                    lat = gps.get(piexif.GPSIFD.GPSLatitude)
                    lat_ref = gps.get(piexif.GPSIFD.GPSLatitudeRef)
                    lon = gps.get(piexif.GPSIFD.GPSLongitude)
                    lon_ref = gps.get(piexif.GPSIFD.GPSLongitudeRef)
                    if all([lat, lat_ref, lon, lon_ref]):
                        data["gps"] = {
                            "latitude": convert_gps(lat, lat_ref),
                            "longitude": convert_gps(lon, lon_ref)
                        }
    except Exception as e:
        data["error"] = str(e)
    return data

@app.route("/extract", methods=["POST"])
def extract():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400
        
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)
    
    result = process_image(filepath, file.filename)
    
    try:
        os.remove(filepath)
    except:
        pass
        
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
