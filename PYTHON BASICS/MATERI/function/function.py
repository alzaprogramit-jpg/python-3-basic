print("MATERI 8 - Function Basic")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# buat fungsi dengan "def" lalu nama fungsinya
# parameter "nama" untuk mengambil nilai dari luar sisi fungsi
def hallo_dunia(nama):
    print("selamat datang")
    print("hallo Mr. ", nama)
print("---------------->")

# panggil nama fungsi di sertai ()
hallo_dunia("baihaqy")
hallo_dunia("dzulhaq")
hallo_dunia("alza")
hallo_dunia("luthbay")
# fungsi luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    print("p =", panjang)
    print("L =", lebar)
    rumus = panjang * lebar
    print("hasil luas persegi panjang =", rumus)

luas_persegi_panjang(10, 5)
luas_persegi_panjang(8, 100)
# def luas segitiga