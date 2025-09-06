import requests
url = "https://api.aladhan.com/v1/timingsByCity/{tanggal}city={kota}ta&country=Indonesia&method=5"
response = requsts.get(url) # HTTP GET
data_json = response.json() # Konversi ke JSON
jadwal_sholat = data_json['data']['timings']
tgl_hijri= data_json['data']['date']['hijri']['date']
print(f"tgl_hijri: {tgl_hijri}")
print("jadwal sholat:")
print(f"-> shubuh:{jadwal jadwal_sholat['fajr']}")