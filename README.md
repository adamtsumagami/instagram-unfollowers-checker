# 📸 IG Unfollowers Checker

Script Python sederhana untuk mengecek siapa saja yang tidak mem-follow balik akun Instagram kamu. Menggunakan [Instaloader](https://instaloader.github.io/), sesi login akan disimpan secara lokal sehingga hanya perlu login sekali.

---

## ✨ Fitur

- 🔍 Mengecek siapa yang tidak follow kamu balik
- 📥 Mengambil daftar followers dan following
- 🔐 Otentikasi via session Instaloader
- 📄 Mudah dipasang dan digunakan

---

## ⚙️ Instalasi

1. **Clone repo ini atau download file-nya**
   ```bash
   git clone https://github.com/kamu/instagram-unfollowers-checker.git
   cd ig-unfollowers-checker
2. **Install dependency**
   ```bash
   pip install instaloader
4. **Login ke akun instagram kamu**
   ```bash
   instaloader --login=USERNAME_KAMU

## Cara Menjalankan
Setelah berhasil login, jalankan
```bash
python check_unfollowers.py
```

## Keamanan
Script ini tidak menyimpan password kamu.

Semua sesi disimpan secara lokal oleh instaloader di :

**Windows :**
```bash
C:\Users\USERNAME\AppData\Local\Instaloader\session-USERNAME
```

**Linux/macOS:**
```bash
~/.config/instaloader/session-USERNAME
```

MIT License © 2025 Adam Tsumagami
