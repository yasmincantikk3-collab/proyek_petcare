"""validasi.py - pengecekan input dan data rekam medis."""
from datetime import datetime

class DataTidakValidError(Exception):
    """Exception buatan sendiri: dimunculkan saat data tidak valid."""
    pass

def validasi_teks(nilai, nama_field):
    """Memastikan teks tidak kosong dan tidak mengandung pemisah ';'." ""
    if nilai is None or not str(nilai).strip():
        raise DataTidakValidError(f"Field '{nama_field}' tidak boleh kosong.")
    teks = str(nilai).strip()
    if ";" in teks:
        raise DataTidakValidError(f"Field '{nama_field}' tidak boleh mengandung ';'.")
    return teks

def validasi_biaya(nilai):
    """Mengubah nilai menjadi float, menolak angka negatif atau bukan angka."""
    try:
        biaya = float(nilai)
    except (ValueError, TypeError):
        raise DataTidakValidError(f"Biaya harus berupa angka, diterima: {nilai!r}")
    if biaya < 0:
        raise DataTidakValidError("Biaya perawatan tidak boleh negatif.")
    return biaya

def validasi_tanggal(nilai):
    """Memastikan tanggal berformat YYYY-MM-DD."""
    try:
        datetime.strptime(str(nilai), "%Y-%m-%d")
    except ValueError:
        raise DataTidakValidError(f"Tanggal harus berformat YYYY-MM-DD, diterima: {nilai!r}")
    return str(nilai)

def validasi_record(**data):
    """Memvalidasi satu record. Atribut diterima lewat **kwargs."""
    for field in ("tanggal", "nama_hewan", "jenis", "layanan", "biaya"):
        if field not in data:
            raise DataTidakValidError(f"Field '{field}' tidak ditemukan.")
    return {
        "tanggal": validasi_tanggal(data["tanggal"]),
        "nama_hewan": validasi_teks(data["nama_hewan"], "nama_hewan").title(),
        "jenis": validasi_teks(data["jenis"], "jenis").title(),
        "layanan": validasi_teks(data["layanan"], "layanan"),
        "biaya": validasi_biaya(data["biaya"])
    }
