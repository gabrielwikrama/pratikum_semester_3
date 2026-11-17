# class Buah:
#     def __init__(self, nama: str, harga: float):
#         self.nama = nama
#         self.harga = harga

# class keranjang:
#     def __init__(self):
#         self.daftar_buah = []

#     def tambah_buah(self, buah: Buah):
#         self.daftar_buah.append(buah)
#         print(f"{buah.nama}")

#     def hitung_total(self) -> float:
#         total = sum(b.harga for b in self.daftar_buah)
#         return total

# if __name__ == "__main__":
#     b1: Buah = Buah("apel", 15000)
#     b2: Buah = Buah("jeruk", 12000)

# keranjang_saya = keranjang()
# keranjang_saya.tambah_buah(b1)
# keranjang_saya.tambah_buah(b2)

# total_bayar = keranjang_saya.hitung_total()
# print(f"Total_Belanjaan: Rp(total_bayar, 0f)")


class Buah:
    def __init__(self, nama: str, harga: float):
        self.nama = nama
        self.harga = harga


class Keranjang:
    def __init__(self):
        self.daftar_buah: list[Buah] = []

    def tambah_buah(self, buah: Buah) -> None:
        self.daftar_buah.append(buah)
        print(f"Menambahkan: {buah.nama} (Rp{buah.harga:,.0f})")

    def hitung_total(self) -> float:
        return sum(b.harga for b in self.daftar_buah)


if __name__ == "__main__":
    b1: Buah = Buah("apel", 15000)
    b2: Buah = Buah("jeruk", 12000)

    keranjang_saya = Keranjang()
    keranjang_saya.tambah_buah(b1)
    keranjang_saya.tambah_buah(b2)

    total_bayar = keranjang_saya.hitung_total()
    print(f"Total Belanjaan: Rp{total_bayar:,.0f}")