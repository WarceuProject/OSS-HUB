# 📦 OSS Hub — Base Repository

Warceu Hub adalah **base repository resmi** milik Warceu Project yang berfungsi sebagai pusat kumpulan project kontributor, template struktur project, serta standar pengembangan dalam ekosistem Warceu.

Repository ini digunakan sebagai media kolaborasi komunitas sebelum project disinkronkan ke repository resmi Warceu.

---

## 🎯 Tujuan

* Menjadi hub project kontributor Warceu
* Menyediakan base repository untuk project baru
* Menstandarkan struktur dan workflow project
* Mempermudah kolaborasi developer
* Menjaga aktivitas kontribusi tetap aktif

---

## 🧩 Fungsi Repository

* Hub project kontributor
* Template struktur project
* Base repository pengembangan
* Standarisasi integrasi ke layanan Warceu (termasuk SSO ke depan)

---

## 👨‍💻 Cara Kontribusi

1. Fork repository ini
2. Buat branch baru untuk project / fitur

```
feature/nama-project
```

3. Tambahkan project menggunakan base repository ini
4. Commit perubahan dengan message yang jelas
5. Submit Pull Request untuk direview maintainer

---

## 📌 Aturan Kontribusi

* ❌ Tidak boleh commit langsung ke `main`
* ✅ Semua perubahan wajib melalui Pull Request
* ✅ Setiap project berada di branch terpisah
* ✅ Gunakan struktur base repository
* ✅ Ikuti standar Warceu Project

---

## ⏱️ Aktivitas Kontributor

Setelah Pull Request dibuat:

* Kontributor wajib melakukan commit minimal **1x setiap minggu** jika project masih dalam pengembangan
* Project yang tidak aktif dapat diarsipkan
* Maintainer berhak menutup PR yang tidak aktif

---

## 📁 Contoh Struktur Project

```
projects/
 ├── project-a/
 │   ├── README.md
 │   ├── app/
 │   └── config/
 └── project-b/
```

---

## 🔗 Integrasi Layanan Warceu (Konsep)

Project yang berada di Warceu Hub harus:

* Mengikuti struktur base repository
* Menyiapkan konfigurasi integrasi layanan (config / env / adapter)
* Mengikuti standar Warceu untuk integrasi ke depan
* Siap dihubungkan ke layanan utama Warceu (SSO, API, platform, dll)

Implementasi integrasi layanan dapat dilakukan bertahap sesuai perkembangan project.

---

## 🧑‍⚖️ Role

### Maintainer

* Review Pull Request
* Menentukan standar repository
* Merge / archive project
* Sinkronisasi ke repository resmi

### Contributor

* Menambahkan project
* Mengembangkan project dari base repository
* Menjaga aktivitas kontribusi

---

## ✅ Repository Resmi

⚠️ **Perhatian**

Repository resmi Warceu Project telah dialihkan ke:

🔗 https://git.warceuproject.or.id

GitHub digunakan sebagai media kolaborasi dan kontribusi komunitas.

---

## 🤝 Kontribusi

Kami tidak menerima push langsung ke repository resmi.

Semua kontribusi harus melalui workflow berikut:

1. Fork repository
2. Buat branch baru
3. Commit perubahan
4. Submit Pull Request untuk direview maintainer

Pull Request yang telah disetujui akan diproses dan disinkronkan ke repository resmi.

---

## 🚀 Visi

Membangun ekosistem Warceu yang terstruktur, kolaboratif, dan siap terintegrasi antar layanan melalui standar repository yang konsisten.

---

## 📜 License



```
WPCL(v1.0) License

Warceu Project Community License (WPCL) v1.0

Copyright (c) All contributors

Permission is granted, free of charge, to use, copy, and modify this software,
provided that:

1. **Non-Commercial Use Only**  
   This project may not be used for personal profit, resale, or commercial services without collective consent of the Warceu community.

2. **Attribution**  
   You must give credit to the community and contributors of Warceu Project in any public or derived use.

3. **No Individual Ownership**  
   All contributions are collective. No single contributor may claim ownership of any part.

4. **Community Governance**  
   All major changes or redistribution must be discussed and approved collectively by the Warceu Project community.

5. **Preserve this License**  
   All copies or derivatives must include this license.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
see also: https://github.com/WarceuProject/.github

```
