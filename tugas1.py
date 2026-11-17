# ==========================================
# Tugas Praktikum 01: Sistem Perpustakaan
# ==========================================

class Buku:
    def __init__(self, judul: str, penulis: str, tahun_terbit: int):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def info(self) -> str:
        """Mengembalikan representasi teks informasi buku."""
        return f"'{self.judul}' karya {self.penulis} ({self.tahun_terbit})"


class Perpustakaan:
    def __init__(self, nama_perpustakaan: str):
        self.nama_perpustakaan = nama_perpustakaan
        self.koleksi_buku = []

    def tambah_buku(self, buku: Buku):
        """Menambahkan objek Buku ke dalam daftar koleksi."""
        self.koleksi_buku.append(buku)
        print(f"[+] Berhasil menambahkan: {buku.judul}")

    def tampilkan_buku(self):
        """Menampilkan seluruh daftar buku yang tersimpan."""
        print(f"\n=== Daftar Buku di {self.nama_perpustakaan} ===")
        if not self.koleksi_buku:
            print("Perpustakaan masih kosong.")
            return

        for nomor, buku in enumerate(self.koleksi_buku, start=1):
            print(f"{nomor}. Judul        : {buku.judul}")
            print(f"   Penulis      : {buku.penulis}")
            print(f"   Tahun Terbit : {buku.tahun_terbit}")
            print("-" * 35)


# ==========================================
# Program Utama (Driver Code)
# ==========================================
if __name__ == "__main__":
    perpus = Perpustakaan("Perpustakaan Kampus")

    buku1 = Buku("Struktur Data dan Algoritma", "Adam Drozdek", 2013)
    buku2 = Buku("Clean Code", "Robert C. Martin", 2008)
    buku3 = Buku("Python Crash Course", "Eric Matthes", 2019)

    print("--- Proses Pemasukan Buku ---")
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)
    perpus.tambah_buku(buku3)

    perpus.tampilkan_buku()