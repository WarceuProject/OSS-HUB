##Image Metadata Extractor (IME)

📸 Image Metadata Extractor API adalah REST API berbasis Flask untuk mengekstrak metadata gambar (EXIF), melakukan analisis statistik sederhana, serta memberikan indikasi kemungkinan gambar telah dimodifikasi.

API ini ringan dan hanya menggunakan Pillow + Piexif (tanpa OpenCV).

---

##✨ Fitur

- Ekstraksi metadata EXIF (Make, Model, Timestamp, dll)
- Konversi koordinat GPS ke latitude & longitude desimal
- Analisis statistik gambar (brightness & distribusi warna)
- Deteksi indikasi metadata stripping
- Identifikasi kemungkinan software editing dari tag EXIF
- REST API dengan response JSON

---

🛠 Tech Stack

- Python 3.10+
- Flask
- Pillow (PIL)
- Piexif
- Werkzeug

---

📥 Instalasi

«Penting: "app.py" berada di branch "Lilith-VnK-patch-1" dan di dalam folder "IME/".»

1. Clone repository

git clone https://github.com/Lilith-VnK/IME.git
cd IME

2. Checkout branch

git checkout Lilith-VnK-patch-1

3. Masuk ke folder aplikasi

cd IME

Struktur direktori:

IME/
 └── IME/
      └── app.py

4. Install dependencies

pip install flask pillow piexif werkzeug

5. Jalankan server

python app.py

Jika berhasil:

Running on http://127.0.0.1:5000

---

🚀 Penggunaan API

Endpoint

POST /extract

Request

- Method: POST
- Content-Type: multipart/form-data
- Key: "image"
- Value: file gambar (jpg/jpeg/png)

Contoh Request (cURL)

curl -X POST -F "image=@foto.jpg" http://127.0.0.1:5000/extract

Contoh Response

{
  "analysis": {
    "is_modified": true,
    "software_detected": ["adobe photoshop"]
  },
  "format": "JPEG",
  "width": 1920,
  "height": 1080,
  "Make": "Canon",
  "Model": "EOS R5",
  "gps": {
    "latitude": -6.2088,
    "longitude": 106.8456
  }
}

---

##⚙️ Catatan Teknis

- Batas maksimal upload: 20MB
- Format didukung: JPG, JPEG, PNG
- PNG biasanya tidak menyimpan EXIF kamera selengkap JPEG
- Hasil analisis bersifat indikasi heuristik, bukan bukti forensik hukum

---

##🤝 Kontribusi

Silakan fork repositori dan buat pull request untuk:

- peningkatan akurasi analisis
- penambahan endpoint baru
- optimasi performa
