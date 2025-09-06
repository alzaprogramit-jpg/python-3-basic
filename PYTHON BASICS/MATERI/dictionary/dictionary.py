print("materi ke 7 - python data structure")
print("====================================")
# SET -> { } -> TIDAK BERURUTAN, BERUBAH, TIDAK DUPLIKAT
game_ridho = {"genshin", "mlbb", "delta force"}
game_imam = {"valorant, poin blank"}
# .dd() -> untuk menambah item ke set
game_imam.add("valorant") # jika ada akan di skip
game_imam.add("mlbb")
game_imam.add("genshin")
# .remove() -> menghapus item dari set
game_ridho.remove("mlbb")
# len() -> untuk menghitung jumlah item
print("ridho ada", len(game_ridho), "=>", game_ridho)
print("imam ada", len(game_imam), "=>", game_imam) 
# .union() menggabungkan 2 set yang berbeda
game_gabungan = game_imam.union(game_ridho)
total_game = len(game_gabungan)
print("game gabungan", total_game , "=>", game_gabungan)
# menggabungkan 2 set berbeda
# .intersection() mencari item  yang kembar dari 2 set yang berbeda
# .difference() mencari item yang berbeda dari 2 set yang berbeda
game_kembar = game_ridho.intersection(game_imam)
game_beda = game_ridho.difference(game_imam)
print("game kembar:", game_kembar)
print("game berbeda:", game_beda)
print("-------------DICT-------------")
# Dict (dictionary) -> {key:valeu} / {kunci:isinya}
# berurutan berdasarkan key, berubah, key tidak duplikat
daftar_anime = {
    "jujutsu_kaisen": "gojo satoru",
    "blak_clover": "yami sukehiro",
    "one_punch_man": "saitama",
    "jigoku_raku": "sagiri",
    "naruto": "shikamu",
    "waifu" : {
        "demon_slayer": "mitsuri",
        "spy_x_family": "anya",
        "naruto": "kakashi"
    }
}
print("daftar anime:", daftar_anime)
print("MC ONE PUNCH MAN:", daftar_anime ["one_punch_man"])
print("waifu loli: ", daftar_anime["waifu"]["spy_x_family"])
# mengubah item value berdasarkan key
daftar_anime["one_punch_man"] = "genos"
daftar_anime["waifu"]["demon_slayer"] = "nezuko"
print('MC ONE PUNCH MAN BARU:', daftar_anime["one_punch_man"])
print("waifu loli bisa gede:", daftar_anime["waifu"]["demon_slayer"])
# menambah item value berdasarkan key
daftar_anime["wind_breaker"] = "sakura" 
print("MC wind breaker:", daftar_anime['wind_breaker'])