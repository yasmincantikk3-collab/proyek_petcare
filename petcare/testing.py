"""testing.py - unit testing untuk seluruh modul petcare."""
import unittest
from petcare.processing import total_biaya_tindakan, RekamMedis, AnalisisKlinik, buat_record
from petcare.validasi import DataTidakValidError, validasi_biaya
from petcare.fileio import buat_file_data, tambah_data, baca_data, tulis_laporan

class TestPetCare(unittest.TestCase):
    def test_total_pengeluaran_args(self):
        self.assertEqual(total_biaya_tindakan(150000, 75000), 225000)

    def test_jumlah_negatif_memunculkan_error(self):
        with self.assertRaises(DataTidakValidError):
            validasi_biaya(-1000)

    def test_field_kosong_memunculkan_error(self):
        with self.assertRaises(DataTidakValidError):
            buat_record(tanggal="2026-10-01", nama_hewan="", jenis="Kucing", layanan="Vaksin", biaya="150000")

    def test_buat_file_mode_x_tidak_menimpa(self, path="test_db.txt"):
        buat_file_data(path, "data_awal\n")
        hasil = buat_file_data(path, "data_baru\n")
        self.assertFalse(hasil)

    def test_tambah_data_mode_a(self, path="test_db.txt"):
        rm = RekamMedis("2026-10-01", "Milo", "Kucing", "Vaksin", 150000)
        tambah_data(path, rm)
        data = baca_data(path)
        self.assertGreaterEqual(len(data), 1)

    def test_baris_rusak_dilewati(self, path="test_rusak.txt"):
        with open(path, "w", encoding="utf-8") as f:
            f.write("2026-10-01;Milo;Kucing;Vaksin;150000\n")
            f.write("baris_rusak_abc\n")
            f.write("2026-10-02;Bobby;Anjing;Grooming;100000\n")
        data = baca_data(path)
        self.assertEqual(len(data), 2)

    def test_file_tidak_ada_tidak_crash(self):
        data = baca_data("file_pasti_tidak_ada.txt")
        self.assertEqual(data, [])

    def test_rekap_dan_kategori_terboros(self):
        r1 = RekamMedis("2026-10-01", "Milo", "Kucing", "Vaksin", 150000)
        r2 = RekamMedis("2026-10-01", "Bobby", "Anjing", "Grooming", 100000)
        analisis = AnalisisKlinik([r1, r2])
        self.assertEqual(analisis.total_pendapatan(), 250000)
        self.assertEqual(len(analisis.layanan_termahal(1)), 1)

    def test_cari_dengan_kwargs(self):
        r1 = RekamMedis("2026-10-01", "Milo", "Kucing", "Vaksin", 150000)
        analisis = AnalisisKlinik([r1])
        hasil = analisis.cari_berdasarkan_jenis(jenis="Kucing")
        self.assertEqual(len(hasil), 1)

    def test_tulis_laporan_mode_w(self, path="test_laporan.txt"):
        tulis_laporan(path, "Laporan Baru")
        with open(path, "r", encoding="utf-8") as f:
            isi = f.read()
        self.assertEqual(isi, "Laporan Baru")

if __name__ == "__main__":
    unittest.main()
