<<<<<<< HEAD
<div align="center">

# 🚀 Universal OCR REST API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-2.7-blue?style=for-the-badge&logo=paddlepaddle)](https://github.com/PaddlePaddle/PaddleOCR)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)](LICENSE)
[![Linux](https://img.shields.io/badge/Linux-Friendly-green?style=for-the-badge&logo=linux)](https://www.linux.org/)
[![macOS](https://img.shields.io/badge/macOS-Compatible-grey?style=for-the-badge&logo=apple)](https://www.apple.com/)

---

<img src="https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif" width="300" alt="OCR Animation">

**Lightweight & Powerful OCR REST API** built with **FastAPI** and **PaddleOCR**

*Transform documents into text with ease* 📝✨
=======
# 🖼️ Image Enhancement API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green?style=flat-square&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

**Powerful image enhancement service with AI-powered upscaling, denoising, and face restoration**

[Features](#-fitur-utama) • [Installation](#-instalasi) • [Usage](#-cara-penggunaan) • [API Docs](#-dokumentasi-api)
>>>>>>> sumber-sso/Encancher-image

</div>

---

<<<<<<< HEAD
## 📋 Quick Overview

Supports multiple file formats for comprehensive document processing:

* 🖼️ **Images**: `jpg`, `png`, `jpeg`, `webp`
* 📄 **PDF** files (multi-page)
* 📝 **DOC / DOCX** documents

**Perfect for:**

* ✅ Local deployment
* ✅ GitHub Codespaces
* ✅ Self-hosted AI pipelines
* ✅ Automation & OSINT workflows
* ✅ Enterprise document processing

---

## ✨ Features

<table>
  <tr>
    <td>⚡ FastAPI high-performance API</td>
    <td>📚 Multi-page PDF support</td>
  </tr>
  <tr>
    <td>🧠 PaddleOCR deep learning</td>
    <td>📝 DOCX → PDF auto conversion</td>
  </tr>
  <tr>
    <td>🐧 Linux friendly</td>
    <td>📖 Paragraph reconstruction</td>
  </tr>
  <tr>
    <td>🍎 macOS compatible</td>
    <td>☁️ Codespaces ready</td>
  </tr>
</table>

---

## 🧠 Tech Stack

```
┌─────────────────────────────────────┐
│     Universal OCR REST API          │
├─────────────────────────────────────┤
│  🔵 FastAPI          - API Framework │
│  🧠 PaddleOCR        - OCR Engine    │
│  🏹 PaddlePaddle     - ML Framework  │
│  📷 OpenCV           - Image Proc    │
│  📄 pdf2image        - PDF Convert   │
│  🖋️  LibreOffice      - Doc Convert  │
│  ⚙️  Poppler          - PDF Tools    │
└─────────────────────────────────────┘
```

---

## 📦 Supported Formats

| Format | Status | Notes |
|--------|--------|-------|
| JPG 🖼️  | ✅ Supported | Recommended |
| PNG 🖼️  | ✅ Supported | Lossless |
| WEBP 🖼️ | ✅ Supported | Modern format |
| JPEG 🖼️ | ✅ Supported | Compatible |
| PDF 📄  | ✅ Supported | Multi-page |
| DOC 📝  | ✅ Supported | Auto-convert |
| DOCX 📝 | ✅ Supported | Auto-convert |

---

## 🖥️ Installation Guide

### 📥 Clone Repository

```bash
git clone https://github.com/yourusername/universal-ocr-api.git
cd universal-ocr-api
=======
## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Instalasi](#-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Dokumentasi API](#-dokumentasi-api)
- [Model yang Digunakan](#-model-yang-digunakan)
- [Kontribusi](#-kontribusi)

---

## 🎯 Tentang Proyek

**Image Enhancement API** adalah layanan REST API yang dibangun dengan **FastAPI** untuk meningkatkan kualitas gambar menggunakan teknologi AI terkini. Proyek ini mengintegrasikan model-model canggih seperti **RealESRGAN** untuk upscaling dan **GFPGAN** untuk restorasi wajah.

Sempurna untuk:
- 📸 Meningkatkan resolusi foto lama atau berkualitas rendah
- 🔨 Menghilangkan noise dan blur pada gambar
- 👤 Memperbaiki dan meningkatkan detail wajah
- 🤖 Pemrosesan batch otomatis

---

## ✨ Fitur Utama

| Fitur | Deskripsi | Scale |
|-------|-----------|-------|
| 🔝 **Enhance (Upscale)** | Meningkatkan resolusi gambar dengan kualitas tinggi | 4x |
| 🎨 **Denoise** | Menghilangkan noise dan artifact pada gambar | Smart |
| 👤 **Face Fix** | Restorasi dan peningkatan detail wajah | Adaptive |

### Keunggulan
- ⚡ **Cepat & Efisien** - Dioptimalkan untuk performa maksimal
- 🧠 **AI-Powered** - Menggunakan deep learning terbaru
- 🔄 **Real-time Processing** - Respons cepat dengan streaming
- 📦 **Mudah Diintegrasikan** - REST API yang sederhana
- 💻 **Cross-platform** - Berjalan di Windows, macOS, Linux

---

## 🖥️ Persyaratan Sistem

### Hardware (Minimal)
- CPU: Intel i5 / AMD Ryzen 5 atau lebih tinggi
- RAM: 8GB minimum (16GB recommended)
- Storage: 2GB untuk model + space untuk processing

### Hardware (Optimal)
- GPU: NVIDIA dengan 4GB+ VRAM (CUDA compatible)
- RAM: 16GB+
- Storage: SSD dengan 10GB+ space

### Software
- Python 3.8+
- pip / conda package manager
- Optional: CUDA 11.8+ untuk GPU acceleration

---

## 🚀 Instalasi

### Step 1: Clone Repository
```bash
cd /home/rynz/proyek/ocr
```

### Step 2: Buat Virtual Environment
```bash
# Menggunakan venv
python -m venv venv

# Aktivasi environment
## Linux/macOS
source venv/bin/activate
## Windows
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download Model-Model AI
```bash
python download.py
```

Tunggu hingga semua model terunduh (±2-3 menit tergantung internet):
- ✅ RealESRGAN_x4plus.pth (~65MB)
- ✅ GFPGANv1.3.pth (~350MB)
- ✅ Detection & Parsing models (~280MB)

### Step 5: Jalankan API Server
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

✅ Server siap di: **http://localhost:8000**

---

## 📖 Cara Penggunaan

### Melalui Interactive API Documentation
```
http://localhost:8000/docs
```

### Melalui Python Script
```python
import requests
from pathlib import Path

# Setup
API_URL = "http://localhost:8000"
image_path = "path/to/your/image.jpg"

# Baca gambar
with open(image_path, "rb") as f:
    files = {"file": f}
    
    # Upscale gambar
    response = requests.post(f"{API_URL}/enhance", files=files)
    
    # Simpan hasil
    with open("enhanced.png", "wb") as out:
        out.write(response.content)
    
    print("✅ Gambar berhasil ditingkatkan!")
```

### Melalui cURL
```bash
# Enhance (Upscale)
curl -X POST "http://localhost:8000/enhance" \
  -F "file=@image.jpg" \
  -o enhanced.png

# Denoise
curl -X POST "http://localhost:8000/denoise" \
  -F "file=@image.jpg" \
  -o denoised.png

# Face Fix
curl -X POST "http://localhost:8000/facefix" \
  -F "file=@image.jpg" \
  -o facefix.png
```

### Contoh dengan JavaScript/Fetch
```javascript
async function enhanceImage(imageFile) {
  const formData = new FormData();
  formData.append("file", imageFile);
  
  const response = await fetch("http://localhost:8000/enhance", {
    method: "POST",
    body: formData
  });
  
  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  
  // Display hasil
  document.getElementById("result").src = url;
}
```

---

## 🔌 Dokumentasi API

### 1. Health Check
```http
GET /
```
**Response:**
```json
{
  "status": "running"
}
```

### 2. Enhance (Upscaling 4x)
```http
POST /enhance
Content-Type: multipart/form-data

file: <image_file>
```

**Deskripsi:** Meningkatkan resolusi gambar 4x menggunakan RealESRGAN dengan kualitas tinggi

**Supported Format:** JPG, PNG, WebP, BMP
**Max Size:** 50MB
**Output:** PNG

---

### 3. Denoise
```http
POST /denoise
Content-Type: multipart/form-data

file: <image_file>
```

**Deskripsi:** Menghilangkan noise sambil mempertahankan detail

**Konfigurasi:**
- Strength: 0.5 (medium)
- Preserves: Edge detail

---

### 4. Face Fix
```http
POST /facefix
Content-Type: multipart/form-data

file: <image_file>
```

**Deskripsi:** Restorasi wajah dengan background upscale

**Features:**
- 👤 Deteksi wajah otomatis
- ✨ Peningkatan detail wajah
- 🔄 Background enhancement

---

## 🤖 Model yang Digunakan

### 🔝 RealESRGAN x4plus
```
┌─────────────────────────────────────┐
│   RealESRGAN x4 Plus (General)      │
├─────────────────────────────────────┤
│ Input:      Any real-world image    │
│ Output:     4x upscaled image       │
│ Quality:    Very High               │
│ Speed:      Fast (~2-5 sec)         │
│ Size:       ~65 MB                  │
│ Use Case:   General image upscaling │
└─────────────────────────────────────┘
```

### 🎨 GFPGAN v1.3
```
┌─────────────────────────────────────┐
│   GFPGAN v1.3 (Face Enhancement)    │
├─────────────────────────────────────┤
│ Input:      Images dengan wajah     │
│ Output:     Enhanced face + BG      │
│ Upscale:    2x + 4x background      │
│ Quality:    Excellent               │
│ Size:       ~350 MB                 │
│ Use Case:   Face restoration        │
└─────────────────────────────────────┘
```

### 🔍 Supporting Models
- **Resnet50:** Face detection (~50MB)
- **ParseNet:** Face parsing (~80MB)

---

## 📊 Performa

| Operasi | GPU (RTX 3060) | CPU (i5-10400) | Rekomendasi |
|---------|----------------|----------------|------------|
| Enhance (1080p) | ~2 sec | ~8-10 sec | GPU |
| Denoise (1080p) | ~1 sec | ~5 sec | GPU |
| Face Fix (1080p) | ~3 sec | ~15-20 sec | GPU |

---

## 📁 Struktur Proyek

```
ocr/
├── app.py                 # Main FastAPI application
├── download.py            # Model downloader
├── requirements.txt       # Python dependencies
├── README.md             # Dokumentasi ini
├── weights/              # Model weights directory
│   ├── RealESRGAN_x4plus.pth
│   └── GFPGANv1.3.pth
└── gfpgan/              # GFPGAN package
    └── weights/
        ├── detection_Resnet50_Final.pth
        └── parsing_parsenet.pth
```

---

## 🛠️ Troubleshooting

### ❌ Error: "No module named 'fastapi'"
```bash
pip install --upgrade fastapi uvicorn
```

### ❌ CUDA Out of Memory
Gunakan CPU atau hitung tile size:
```python
# Di app.py, ubah tile=0 menjadi:
tile=400  # Process 400x400 tiles
```

### ❌ Model Download Timeout
Download manual dari:
- [RealESRGAN](https://github.com/xinntao/Real-ESRGAN/releases)
- [GFPGAN](https://github.com/TencentARC/GFPGAN/releases)

### ❌ CORS Issues
Tambahkan di app.py:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
>>>>>>> sumber-sso/Encancher-image
```

---

<<<<<<< HEAD
## 🐧 Linux Installation

### 🏹 **Arch Linux**

Install system dependencies:

```bash
sudo pacman -S python python-pip poppler libreoffice-fresh
```

Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install Python packages:

```bash
pip install -U pip
pip install -r requirements.txt
```

Run API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

### 🟣 **Ubuntu / Debian**

Install dependencies:

```bash
sudo apt update
sudo apt install -y python3 python3-venv poppler-utils libreoffice
```

Setup environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🍎 macOS Installation

Install Homebrew first: https://brew.sh

Install dependencies:

```bash
brew install poppler libreoffice
```

Setup Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## ☁️ GitHub Codespaces

Create new Codespace and run:

```bash
sudo apt update
sudo apt install -y poppler-utils libreoffice
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Access API documentation:

```
https://PORT-preview.app.github.dev/docs
```

---

## 🌐 API Usage

### 📍 Home Endpoint

**GET** `/`

Check if API is running:

```json
{
  "message": "Universal OCR API Ready"
}
```

---

### 🔍 OCR Endpoint

**POST** `/ocr`

Upload file using multipart form data for OCR processing.

**Supported Files:**
- Images (jpg, png, jpeg, webp)
- PDF files
- DOC/DOCX documents

---

### 💻 Example CURL Commands

**Process PDF:**
```bash
curl -X POST \
  -F "file=@document.pdf" \
  http://localhost:8000/ocr
```

**Process Image:**
```bash
curl -X POST \
  -F "file=@photo.jpg" \
  http://localhost:8000/ocr
```

**Process Document:**
```bash
curl -X POST \
  -F "file=@report.docx" \
  http://localhost:8000/ocr
```

---

## 📤 API Response Example

```json
{
  "filename": "document.pdf",
  "total_pages": 1,
  "pages": [
    {
      "page": 1,
      "text": "Detected paragraph text reconstructed and organized here..."
    }
  ]
}
```

---

## 📁 Project Structure

```
.
├── main.py                          # FastAPI application
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── __pycache__/                     # Python cache
```

---

## ⚠️ System Requirements

**Python:** 3.10 or higher (3.11+ recommended)

**Hardware:**
- ✅ CPU-only mode supported
- ⭐ GPU optional (CUDA/cuDNN for speedup)
- 💾 Minimum 4GB RAM
- 🔄 SSD recommended for better performance

**Storage:**
- ~2GB for model downloads
- ~1GB for dependencies

---

## 🧩 Troubleshooting

### ❌ numpy / cv2 Error

Recreate environment from scratch:

```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

### ❌ PDF Processing Not Working

Ensure Poppler is installed:

**Arch Linux:**
```bash
sudo pacman -S poppler
```

**Ubuntu/Debian:**
```bash
sudo apt install poppler-utils
```

**macOS:**
```bash
brew install poppler
```

---

### ❌ DOCX File Not Processing

Ensure LibreOffice is installed:

**Arch Linux:**
```bash
sudo pacman -S libreoffice-fresh
```

**Ubuntu/Debian:**
```bash
sudo apt install libreoffice
```

**macOS:**
```bash
brew install libreoffice
```

---

### ❌ Port Already in Use

Use different port:

```bash
uvicorn main:app --host 0.0.0.0 --port 8001
```

---

## 🚀 Roadmap

- [ ] 🎯 Layout detection
- [ ] 📊 Table OCR
- [ ] 📦 Batch processing
- [ ] 🗄️ Vector database export
- [ ] 🔗 RAG pipeline integration
- [ ] 🌐 Multi-language support
- [ ] 📱 Mobile API client
- [ ] 🐳 Docker containerization

---

## 🔐 Security Best Practices

- Use environment variables for sensitive config
- Validate file uploads (type & size)
- Run behind reverse proxy (nginx/Apache)
- Implement rate limiting
- Use HTTPS in production
- Set appropriate file size limits

---

## 📊 Performance Tips

- Use GPU if available (significant speedup)
- Batch process files for better throughput
- Adjust PDF DPI for quality vs speed tradeoff
- Cache model in memory between requests
- Consider async processing for large files

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📜 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...
```

---

## ⭐ Show Your Support

If this project helped you, please consider:

- ⭐ **Star** the repository
- 🍴 **Fork** and build upon it
- 💬 **Share** with others
- 🚀 **Contribute** improvements
- 🐛 **Report** bugs & issues

**Your support drives development!** 💪

---

## 📞 Support & Contact

- 📧 Email: your-email@example.com
- 🐙 GitHub Issues: [Report Issues](https://github.com/yourusername/universal-ocr-api/issues)
- 💬 Discussions: [Join Discussion](https://github.com/yourusername/universal-ocr-api/discussions)

---

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PaddleOCR GitHub](https://github.com/PaddlePaddle/PaddleOCR)
- [Python Best Practices](https://pep8.org/)
- [REST API Design](https://restfulapi.net/)

---

<div align="center">

### Built with ❤️ for the Community

Made with 🚀 by AI Enthusiasts | 2024

⬆️ [Back to Top](#-universal-ocr-rest-api)

</div>
=======
## 📝 Lisensi

Proyek ini menggunakan model-model dari:
- **RealESRGAN** - [BasicSR](https://github.com/xinntao/BasicSR) (Apache 2.0)
- **GFPGAN** - [Tencent ARC](https://github.com/TencentARC/GFPGAN) (Apache 2.0)

---
=======
# OSS HUB

Welcome to OSS HUB.

OSS HUB is a monorepo from the WarceuProject Community containing a collection of simple projects, experiments, and small open-source works.

⚠️ Note:  
This repository acts as the parent/base of all OSS HUB activities. Development in the root repository is limited. Most development happens inside each subproject directory.

---

## Languages Used

Projects inside OSS HUB may use:

- python  
- nodejs  
- perl  
- ruby  
- c / c++  
- java  
- php  
- javascript (ES)  
- flutter  

---

## Build Tools

Depending on the project:

- meson  
- cmake / GNU Make  

Each project must include its own build and run instructions inside its directory.

---

## Repository Structure

Each folder in the root directory represents a standalone project.

Example:

```
OSS-HUB/
├── project-a/
├── project-b/
└── your-feature/
```

`your-feature` = your standalone subrepository/project.

---

## Contribution Guidelines

1. Fork or clone this repository  
   ⚠️ When forking, **do not change the default repository name**. Keep it as `OSS-HUB`.
2. Create a new branch using **lowercase only**, no camelCase, no spaces, no special characters except `-`:

   ```
   feature/your-feature
   ```

   ❌ Examples of disallowed branch names:  
   - `Feature/MyFeature` (uppercase)  
   - `myFeature` (camelCase)  
   - `my feature` (space)  
   - `feature@123` (special characters)  

3. Create a new directory in the repository root named:

   ```
   your-feature
   ```

4. Put your project inside that directory  
5. Push your changes and open a Pull Request  
6. Wait for review  

Keep it simple. Include a README, and ensure your project builds and runs properly.

---

## Licensing

All projects submitted to OSS HUB **must use the GPL license**.  
Other licenses are not allowed.  

Include a proper `LICENSE` file in your project folder specifying the GPL version you are using.

---

## Engineering Philosophy

We prefer practical and maintainable code over unnecessary complexity.

- **YAGNI** — You Aren't Gonna Need It  
  Don’t build something until it’s actually needed.

- **DRY** — Don’t Repeat Yourself  
  Avoid duplicated logic and redundant code.

- **KISS** — Keep It Simple, Stupid  
  Simple solutions are usually better.

- **SOLID** — Basic object-oriented design principles  
  Write modular, extendable, and maintainable code.

Clean > Clever  
Readable > Smart-looking  
Working > Overengineered  

---

## Ethics & Commit Guidelines

OSS HUB is a community. We value clear, honest, and respectful contributions.

- **Commit Messages**  
  - Must be clear and descriptive.  
  - Include commit hash if referencing previous commits or issues.  
  - Commits with a joke or creative touch are appreciated 😄.  
  - Lazy or meaningless commits will be rejected.  
  - **Follow [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)** for consistency.

- **Behavior**  
  - Respect other contributors  
  - Do not spam or flood the repo  
  - Help others when possible  

- **Collaboration Mindset**  
  - Focus on learning, sharing, and improving together.  
  - Quality over quantity: better to submit one solid PR than five half-baked ones.

---

## Read More

For detailed guidelines and additional information, please read the full documentation:

👉 **[Read more](https://github.com/WarceuProject/OSS-HUB/blob/master/OSSHUB.md)**

>>>>>>> sumber-sso/Encancher-image
