from fastapi import FastAPI, UploadFile, File, HTTPException
from paddleocr import PaddleOCR
from PIL import Image
from pdf2image import convert_from_bytes
import numpy as np
import tempfile
import subprocess
import io
import os
import shutil
import re

app = FastAPI(title="Universal OCR API")

# =============================
# LOAD MODEL SEKALI
# =============================
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    show_log=False
)

# =============================
# SMART PARAGRAPH OCR
# =============================
def run_ocr(pil_image):

    image_np = np.array(pil_image.convert("RGB"))
    result = ocr.ocr(image_np)

    if not result or not result[0]:
        return {"text": ""}

    lines = result[0]

    # ✅ sort top->bottom THEN left->right
    lines = sorted(
        lines,
        key=lambda x: (x[0][0][1], x[0][0][0])
    )

    merged_lines = []

    current_line = ""
    last_y = None

    for line in lines:

        box = line[0]
        text = line[1][0].strip()

        y = box[0][1]

        if last_y is None:
            current_line = text
        else:
            # threshold baris sama
            if abs(y - last_y) < 18:
                current_line += " " + text
            else:
                merged_lines.append(current_line)
                current_line = text

        last_y = y

    if current_line:
        merged_lines.append(current_line)

    # =============================
    # PARAGRAPH CLEANING
    # =============================
    paragraph = " ".join(merged_lines)

    paragraph = re.sub(r"\s+", " ", paragraph)

    paragraph = (
        paragraph
        .replace(" .", ".")
        .replace(" ,", ",")
        .replace(" :", ":")
        .replace(" ;", ";")
    )

    return {"text": paragraph}


# =============================
# IMAGE HANDLER
# =============================
def process_image(contents):

    try:
        image = Image.open(io.BytesIO(contents))
    except Exception:
        raise HTTPException(400, "Invalid image file")

    return [{
        "page": 1,
        **run_ocr(image)
    }]


# =============================
# PDF HANDLER
# =============================
def process_pdf(contents):

    try:
        pages = convert_from_bytes(contents)
    except Exception:
        raise HTTPException(
            500,
            "Poppler not installed or PDF invalid"
        )

    results = []

    for i, page in enumerate(pages):
        results.append({
            "page": i + 1,
            **run_ocr(page)
        })

    return results


# =============================
# DOCX → PDF
# =============================
def convert_docx_to_pdf(contents, filename):

    if shutil.which("libreoffice") is None:
        raise HTTPException(500, "LibreOffice not installed")

    with tempfile.TemporaryDirectory() as tmpdir:

        input_path = os.path.join(tmpdir, filename)

        with open(input_path, "wb") as f:
            f.write(contents)

        try:
            subprocess.run(
                [
                    "libreoffice",
                    "--headless",
                    "--convert-to",
                    "pdf",
                    input_path,
                    "--outdir",
                    tmpdir,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )
        except subprocess.CalledProcessError:
            raise HTTPException(500, "DOCX conversion failed")

        pdf_path = input_path.rsplit(".", 1)[0] + ".pdf"

        if not os.path.exists(pdf_path):
            raise HTTPException(500, "PDF not generated")

        with open(pdf_path, "rb") as f:
            return f.read()


# =============================
# ROUTES
# =============================
@app.get("/")
def home():
    return {"message": "Universal OCR API Ready 🚀"}


@app.post("/ocr")
async def ocr_file(file: UploadFile = File(...)):

    contents = await file.read()

    if not file.filename:
        raise HTTPException(400, "Filename missing")

    filename = file.filename.lower()

    if filename.endswith((".jpg", ".jpeg", ".png", ".webp")):
        pages = process_image(contents)

    elif filename.endswith(".pdf"):
        pages = process_pdf(contents)

    elif filename.endswith((".doc", ".docx")):
        pdf_bytes = convert_docx_to_pdf(contents, filename)
        pages = process_pdf(pdf_bytes)

    else:
        raise HTTPException(400, "Unsupported file format")

    return {
        "filename": file.filename,
        "total_pages": len(pages),
        "pages": pages
    }