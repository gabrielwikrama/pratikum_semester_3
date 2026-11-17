class mahasiswa: 
    jumlah_mahasiswa = 0

    def __init__(self, nama: str, nim: str, ipk: float = 0.0):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        mahasiswa.jumlah_mahasiswa += 1

    def tampilkan_info(self):
        print(f"NIM: {self.nim} | nama: {self.nama} | ipk: {self.ipk:.2f}")