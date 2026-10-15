# CRUD Data Mahasiswa

Aplikasi web sederhana untuk mengelola data mahasiswa (Create, Read, Update, Delete).
UTS Lab Pemrograman, Program Studi Bisnis Digital, Universitas Diponegoro.

## Teknologi
- Python + Flask
- SQLite
- HTML + CSS

## Fitur
- Tambah, lihat, ubah, dan hapus data mahasiswa
- Validasi: NIM/nama/program studi wajib diisi, IPK 0.00-4.00, NIM tidak boleh kembar
- Lama Studi dihitung otomatis (tahun sekarang - angkatan)
- Data tersimpan permanen di database SQLite

## Cara menjalankan
1. Install dependensi: `pip install -r requirements.txt`
2. Jalankan: `python app.py`
3. Buka `http://127.0.0.1:5000`

Database `mahasiswa.db` dibuat otomatis saat aplikasi pertama kali dijalankan.