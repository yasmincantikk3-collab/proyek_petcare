"""processing.py - class data serta perhitungan dan analisis klinik petcare."""
from petcare.validasi import DataTidakValidError, validasi_record

def total_biaya_tindakan(*args_biaya):
    """Menjumlahkan komponen biaya dinamis menggunakan *args."""
    assert all(b >= 0 for b in args_biaya), "Biaya perawatan tidak boleh negatif."
    return sum(args_biaya)

def format_rupiah(angka):
    """Memformat angka menjadi teks rupiah, contoh: Rp150.000."""
    return "Rp" + f"{angka:,.0f}".replace(",", ".")

class Pasien:
    """Class induk untuk data dasar hewan."""
    def __init__(self, tanggal, nama_hewan, jenis):
        self.tanggal = tanggal
        self.nama_hewan = nama_hewan
        self.jenis = jenis

class RekamMedis(Pasien):
    """Class turunan untuk detail rekam medis dan biaya."""
    def __init__(self, tanggal, nama_hewan, jenis, layanan, biaya):
        super().__init__(tanggal, nama_hewan, jenis)
        self.layanan = layanan
        self.biaya = biaya

    def ke_baris(self):
        """Mengubah objek menjadi satu baris teks untuk disimpan ke file."""
        return f"{self.tanggal};{self.nama_hewan};{self.jenis};{self.layanan};{self.biaya}"

    @classmethod
    def dari_baris(cls, baris):
        """Membuat objek dari satu baris teks; error jika format salah."""
        bagian = baris.strip().split(";")
        if len(bagian) != 5:
            raise DataTidakValidError(f"Jumlah kolom harus 5, ditemukan {len(bagian)}")
        tanggal, nama_hewan, jenis, layanan, biaya = bagian
        validated = validasi_record(
            tanggal=tanggal, nama_hewan=nama_hewan, jenis=jenis, layanan=layanan, biaya=biaya
        )
        return cls(**validated)

    def __repr__(self):
        return f"RekamMedis({self.ke_baris()})"

def buat_record(**atribut):
    """Membuat objek RekamMedis dari atribut bervariasi (**kwargs) setelah divalidasi."""
    return RekamMedis(**validasi_record(**atribut))

class AnalisisKlinik:
    """Kumpulan fungsi analisis untuk data rekam medis."""
    def __init__(self, daftar):
        self.daftar = daftar

    def total_pendapatan(self):
        """Total seluruh pendapatan biaya perawatan."""
        return total_biaya_tindakan(*[p.biaya for p in self.daftar])

    def rata_rata_biaya(self):
        """Rata-rata biaya per pasien."""
        if not self.daftar:
            return 0
        return self.total_pendapatan() / len(self.daftar)

    def rekap_per_jenis(self):
        """Dictionary total pendapatan untuk setiap jenis hewan."""
        rekap = {}
        for p in self.daftar:
            rekap[p.jenis] = rekap.get(p.jenis, 0) + p.biaya
        return rekap

    def layanan_termahal(self, n=3):
        """n layanan termahal, diurutkan menurun menggunakan lambda sebagai key."""
        return sorted(self.daftar, key=lambda p: p.biaya, reverse=True)[:n]

    def cari_berdasarkan_jenis(self, **kriteria):
        """Mencari data dengan kriteria bebas menggunakan **kwargs dan filter lambda."""
        return list(filter(
            lambda p: all(getattr(p, k, None) == v for k, v in kriteria.items()),
            self.daftar
        ))

def susun_laporan_klinik(analisis):
    """Menyusun teks laporan dari objek AnalisisKlinik."""
    baris = ["LAPORAN KLINIK PETCARE", "=" * 35]
    baris.append(f"Total Kunjungan Pasien : {len(analisis.daftar)}")
    baris.append(f"Total Pendapatan       : {format_rupiah(analisis.total_pendapatan())}")
    baris.append(f"Rata-rata Biaya/Pasien : {format_rupiah(analisis.rata_rata_biaya())}")
    baris.append("-" * 35)
    baris.append("Rekap Pendapatan per Jenis Hewan:")
    total = analisis.total_pendapatan() or 1
    for jenis, biaya in sorted(analisis.rekap_per_jenis().items(), key=lambda item: item[1], reverse=True):
        baris.append(f" - {jenis:<10}: {format_rupiah(biaya):>10} ({biaya/total*100:.1f}%)")
    baris.append("-" * 35)
    baris.append("3 Layanan/Biaya Terbesar:")
    for p in analisis.layanan_termahal(n=3):  # keyword argument
        baris.append(f" {p.tanggal} | {p.nama_hewan} ({p.jenis}) - {p.layanan}: {format_rupiah(p.biaya)}")
    return "\n".join(baris) + "\n"
