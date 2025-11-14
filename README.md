# Pibal Flask CRUD – A Simple Patient Management Web App

**Proyek ini dibuat oleh:** Iqbal Guntur   
---

## Deskripsi
Aplikasi web sederhana untuk **CRUD data pasien** menggunakan **Flask** (Python) dan **MariaDB**.  
Dijalankan di server **Raspberry Pi 3 B+ (Pibal)**, aplikasi ini memungkinkan:
- Menambahkan pasien baru
- Melihat daftar pasien
- Mengubah data pasien
- Menghapus pasien

---

## Teknologi yang Digunakan
- **Python 3**
- **Flask** – web framework
- **MySQL / MariaDB** – database
- **HTML** – untuk tampilan dasar
- **Bootstrap** (opsional, untuk tampilan lebih rapi)

---

## Struktur Folder
pibal_flask/
│
├── app.py # file utama Flask
├── templates/
│ ├── index.html # halaman list pasien
│ ├── tambah.html # form tambah pasien
│ └── edit.html # form edit pasien

yaml
Salin kode

---

## Instalasi & Setup
1. Clone repository:
```bash
git clone https://github.com/MfBally354/rs_flask1.git
cd rs_flask1
(Opsional tapi direkomendasikan) Buat virtual environment:

bash
Salin kode
python3 -m venv venv
source venv/bin/activate
Install dependensi:

bash
Salin kode
sudo pip install --break-system-packages flask mysql-connector-python
Pastikan MariaDB sudah terinstall dan database sudah dibuat:

sql
Salin kode
CREATE DATABASE pibal_app;
USE pibal_app;
CREATE TABLE pasien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100),
    umur INT
);
Jalankan aplikasi:

bash
Salin kode
python3 app.py
Buka browser:

cpp
Salin kode
http://<IP_PIBAL>:5000/
Cara Menggunakan
Tambah Pasien: Klik tombol Tambah Pasien, isi form, lalu klik Simpan

Edit Pasien: Klik Edit pada pasien yang ingin diubah

Hapus Pasien: Klik Hapus pada pasien yang ingin dihapus

Screenshot
[Tambahkan screenshot halaman index, tambah, edit pasien di sini]

Lisensi
MIT License – bebas digunakan untuk belajar dan proyek pribadi
