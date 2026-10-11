from petcare.fileio import muat_data, simpan_data
from petcare.processing import tambah_rekam_medis, hitung_total_biaya, cari_rekam_medis
from petcare.validasi import validasi_nama

def tampilkan_menu():
    print("\n" + "="*40)
    print("      SISTEM MANAJEMEN PETCARE UTS     ")
    print("="*40)
    print("1. Tampilkan Semua Rekam Medis")
    print("2. Tambah Rekam Medis Baru")
    print("3. Cari Rekam Medis Hewan")
    print("4. Hitung Total Biaya Layanan")
    print("5. Keluar")
    print("="*40)

def main():
    nama_file = "rekam_medis.txt"
    data_pasien = muat_data(nama_file)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == '1':
            print("\n--- DAFTAR REKAM MEDIS ---")
            if not data_pasien:
                print("Belum ada data rekam medis.")
            else:
                for idx, p in enumerate(data_pasien, start=1):
                    print(f"{idx}. ID: {p['id']} | Hewan: {p['nama_hewan']} | Pemilik: {p['pemilik']} | Layanan: {p['layanan']} | Biaya: Rp{p['biaya']:.2f}")

        elif pilihan == '2':
            print("\n--- TAMBAH REKAM MEDIS ---")
            try:
                id_pasien = input("Masukkan ID Pasien (misal: P001): ").strip()
                nama_hewan = validasi_nama(input("Masukkan Nama Hewan: "))
                pemilik = validasi_nama(input("Masukkan Nama Pemilik: "))
                layanan = input("Masukkan Jenis Layanan: ").strip()
                biaya = float(input("Masukkan Biaya Layanan: "))

                tambah_rekam_medis(data_pasien, id=id_pasien, nama_hewan=nama_hewan, pemilik=pemilik, layanan=layanan, biaya=biaya)
                simpan_data(nama_file, data_pasien)
                print("-> Rekam medis berhasil ditambahkan dan disimpan!")
            except Exception as e:
                print(f"[ERROR] Gagal menambah data: {e}")

        elif pilihan == '3':
            print("\n--- CARI REKAM MEDIS ---")
            nama_cari = input("Masukkan nama hewan yang dicari: ").strip()
            hasil = cari_rekam_medis(data_pasien, nama_cari)
            if hasil:
                print(f"Ditemukan {len(hasil)} data:")
                for p in hasil:
                    print(f"- ID: {p['id']} | Hewan: {p['nama_hewan']} | Pemilik: {p['pemilik']} | Layanan: {p['layanan']} | Biaya: Rp{p['biaya']:.2f}")
            else:
                print("Data tidak ditemukan.")

        elif pilihan == '4':
            print("\n--- TOTAL BIAYA LAYANAN ---")
            total = hitung_total_biaya(data_pasien)
            print(f"Total pendapatan layanan PetCare: Rp{total:.2f}")

        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan Sistem Manajemen PetCare!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
