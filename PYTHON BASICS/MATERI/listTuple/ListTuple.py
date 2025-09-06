print("materi ke 6")
print("python data stuctures")
print("tema: list Tuple")
# list pake []
# tuple pake ()
print("---------")
# list -> [ ] -> berurutan, berubah, boleh duplikat 
#List: Koleksi data yang berurutan dan bisa diubah. List ditulis dengan [].
daftar_belanja = [
    "pisang kembung", # index 0
    "es teh desa", # index 1
    "gabin"# index 2
]
print("tas belanja:", daftar_belanja)
# akses item dengan index
print(daftar_belanja[1])
# append() untuk menambah item ke index tertentu
daftar_belanja.insert(1, "batagor")
# remove() untuk menghapus item
daftar_belanja.remove("es teh desa")
print("tas belanja sekarang:", daftar_belanja)
# mesnggabungkan list dengan +
jajanan_ishaq = ["olive chiken", "macaroni", "keripik singkong"]
jajanan_bilal = ["naspad kawan lamo", "indomie", "gorengan"]
titip_belanjaan = jajanan_bilal + jajanan_ishaq
print("titipan_belanja:", titip_belanjaan)
# menggandakan item list dengan *
print("bilal nambah:", jajanan_bilal * 3 )
print("DAFTAR MENU: ")
print("--------------------")
# tuple -> ( ) -> berurutan, tidak berubah, boleh duplikat
ttl = ("taliwang", 19, "juni", 2007)
print("TTL:", ttl)
print("bulan lahir luthbay", ttl[2])
# Unpacking variabel (mengekstrak tuple ke variable baru)
tempat_lahir, tanggal_lahir, bulan_lahir, tahun_lahir = ttl
print("tahun lahir: ", tahun_lahir)
print("===============================================================")


buah_list = ["jeruk", "durian", "blewah", "nanas"]
print(buah_list)

for item in buah_list:
    print(item)
# # operasi pada list

# # 1. menambah data ke dalam list

# append