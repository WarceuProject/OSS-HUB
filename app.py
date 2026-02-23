from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image
import numpy as np
import torch

from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
from gfpgan import GFPGANer

app = FastAPI(title="Image Enhance API")

device = "cpu"

#################################
# LOAD REAL-ESRGAN
#################################

model = RRDBNet(
    num_in_ch=3,
    num_out_ch=3,
    num_feat=64,
    num_block=23,
    num_grow_ch=32,
    scale=4
)

upsampler = RealESRGANer(
    scale=4,
    model_path="weights/RealESRGAN_x4plus.pth",
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=False,
    device=device,
)

#################################
# LOAD GFPGAN
#################################

face_enhancer = GFPGANer(
    model_path="weights/GFPGANv1.3.pth",
    upscale=2,
    arch="clean",
    channel_multiplier=2,
    bg_upsampler=upsampler,
)

#################################
# UTIL
#################################

def pil_to_np(file):
    img = Image.open(BytesIO(file)).convert("RGB")
    return np.array(img)

def np_to_response(img):
    output = Image.fromarray(img)
    buf = BytesIO()
    output.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

#################################
# ENDPOINTS
#################################

@app.get("/")
def root():
    return {"status": "running"}

#################################
# ENHANCE (UPSCALE)
#################################

@app.post("/enhance")
async def enhance(file: UploadFile = File(...)):
    img = pil_to_np(await file.read())
    output, _ = upsampler.enhance(img)
    return np_to_response(output)

#################################
# DENOISE
#################################

@app.post("/denoise")
async def denoise(file: UploadFile = File(...)):
    img = pil_to_np(await file.read())
    output, _ = upsampler.enhance(img, denoise_strength=0.5)
    return np_to_response(output)

#################################
# FACE FIX
#################################

@app.post("/facefix")
async def facefix(file: UploadFile = File(...)):
    img = pil_to_np(await file.read())
    _, _, output = face_enhancer.enhance(
        img,
        has_aligned=False,
        only_center_face=False,
        paste_back=True,
    )
    return np_to_response(output)