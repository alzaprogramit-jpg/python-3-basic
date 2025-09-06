import json
print("materi 12-JSON")
file_json_path = r"C:\PROGRAM IT\GIT\rukun_islam.json"
with open(file_json_path, "r") as file_json:
    data_json = json.load(file_json)
    print(f"judul file: {data_json['judul']}")
    print(f"jumlah rukun islam: {data_json['jumlah']}")
    print(f"daftar rukun islam:")
    for item_rukun in data_json['rukun']:
        print(item_rukun)
print("_" * 45) # buat garis panjang
#tampilkan surah sebagai tabel garis sederhana
#keys: nomor, nama, jumlah_ayat, tempat_turun
print("| No | Nama | Jumlah ayat | Tempat turun")
print("_" * 50)
for surah in data_json['suruh']:
    print(f"{surah['Nomor']}" | {surah['Jumlah_ayat']} | {surah['Tempat turun']})