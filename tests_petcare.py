import unittest
from petcare.processing import RekamMedis, total_biaya_tindakan, AnalisisKlinik
from petcare.validasi import DataTidakValidError, validasi_record

DATA_UJI = [
    RekamMedis("2026-10-01", "Milo", "Kucing", "Vaksin", 150000),
    RekamMedis("2026-10-02", "Bobby", "Anjing", "Grooming", 100000),
]

class TestPetCare(unittest.TestCase):
    def test_total_pengeluaran_args(self):
        self.assertEqual(total_biaya_tindakan(50000, 25000), 75000)

    def test_biaya_negatif_memunculkan_error(self):
        with self.assertRaises(AssertionError):
            total_biaya_tindakan(-1000)

    def test_field_kosong_memunculkan_error(self):
        with self.assertRaises(DataTidakValidError):
            validasi_record(tanggal="2026-10-01", nama_hewan="", jenis="Kucing", layanan="Vaksin", biaya=100000)

    def test_analisis_pendapatan(self):
        analisis = AnalisisKlinik(DATA_UJI)
        self.assertEqual(analisis.total_pendapatan(), 250000)
        self.assertEqual(analisis.rata_rata_biaya(), 125000)

    def test_cari_berdasarkan_kwargs(self):
        analisis = AnalisisKlinik(DATA_UJI)
        hasil = analisis.cari_berdasarkan_jenis(jenis="Anjing")
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0].nama_hewan, "Bobby")

if __name__ == '__main__':
    unittest.main()
