import os
import urllib.request

os.makedirs("weights", exist_ok=True)

models = {
    "realesrgan": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth",
    "gfpgan": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth"
}

for name, url in models.items():
    path = f"weights/{url.split('/')[-1]}"
    if not os.path.exists(path):
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(url, path)

print("Models ready.")