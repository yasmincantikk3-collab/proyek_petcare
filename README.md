# Proyek Ujian Tengah Semester (UTS) - Pemrograman Terstruktur
**Sistem Manajemen Klinik Hewan (Pet Care)**

---

## 📌 Identitas Mahasiswa
* **Nama:** Yasmin
* **NPM:** 2517052008
* **Kelas / Program Studi:** SI-A / S1 Sistem Informasi
* **Universitas:** Universitas Lampung (UNILA)

---

## 📂 Struktur Proyek & Modul
Proyek ini dirancang secara modular menggunakan package Python (`petcare/`) dengan pemisahan tugas (*separation of concerns*):
* `main.py` : Berisi antarmuka menu interaktif utama program.
* `rekam_medis.txt` : Berfungsi sebagai database berbasis file teks (.txt) dengan pemisah titik koma (`;`).
* `petcare/__init__.py` : Penanda bahwa direktori tersebut adalah sebuah package Python.
* `petcare/fileio.py` : Mengelola operasi I/O file (mode `x`, `a`, `r`, `w`) secara aman menggunakan context manager `with open()`.
* `petcare/processing.py` : Berisi class induk (`Pasien`) dan class turunan (`RekamMedis`), serta fungsi analisis klinik (total pendapatan, rata-rata, rekap jenis hewan, layanan termahal, pencarian dengan `**kwargs`).
* `petcare/validasi.py` : Menangani validasi input data, tanggal (`YYYY-MM-DD`), pengecekan angka negatif, serta custom exception (`DataTidakValidError`).
* `petcare/testing.py` : Modul unit testing otomatis menggunakan pustaka `unittest` (mencakup pengujian fungsi, *args, mode file, dan eksepsi).
* `laporan/laporan_klinik.txt` : File keluaran otomatis untuk rekapitulasi laporan klinik.

---

## 🚀 Cara Menjalankan Program
1. Pastikan Python sudah terinstal di komputer Anda.
2. Unduh atau clone repository ini.
3. Buka terminal atau PowerShell pada direktori proyek.
4. Jalankan perintah berikut untuk mengeksekusi program utama:
   ```bash
   python main.py
