class mahasiswa: 
    jumlah_mahasiswa = 0

    def __init__(self, nama: str, nim: str, ipk: float = 0.0):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        mahasiswa.jumlah_mahasiswa += 1

    def tampilkan_info(self):
        print(f"NIM: {self.nim} | nama: {self.nama} | ipk: {self.ipk:.2f}")

if __name__ == "__main__":
    print(f"Jumlah Awal: {mahasiswa.jumlah_mahasiswa}")

    m1 = mahasiswa("Alfan", "240403010051", "3,75")
    m2 = mahasiswa("Josua", "240403010032", "3.45")

    m1.tampilkan_info()
    m2.tampilkan_info()


    print(f"Jumlah Total Mahasiswa: {mahasiswa.jumlah_mahasiswa}")