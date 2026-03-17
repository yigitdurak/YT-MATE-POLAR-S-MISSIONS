kullanici_verileri = [
    {"isim": "Ahmet", "yas": 19},
    {"isim": "Mehmet", "yas": 25},
    {"isim": "Ayşe", "yas": 22},
    {"isim": "Zeynep", "yas": 18},
    {"isim": "Ali", "yas": 30},
    {"isim": "Burak", "yas": 17},
    {"isim": "Cem", "yas": 21},
    {"isim": "Aslı", "yas": 16},
]


filtrelenmis_liste = [
    kullanici
    for kullanici in kullanici_verileri
    if kullanici["yas"] > 20 or kullanici["isim"].startswith(("a", "A"))
]


print("\nFiltrelenmiş Veriler1:", *filtrelenmis_liste)

print("\n\n")


def esnek_veri_filtresi(*args, **kwargs):

    tum_veriler = []
    for liste in args:
        tum_veriler.extend(liste)

    filtrelenmis_sonuc = [
        kullanici
        for kullanici in tum_veriler
        if "min_yas" in kwargs
        and kullanici["yas"] > kwargs["min_yas"]
        or "bas_harf" in kwargs
        and kullanici["isim"].startswith(kwargs["bas_harf"])
    ]

    return filtrelenmis_sonuc


liste1 = [
    {"isim": "Ahmet", "yas": 65},
    {"isim": "Mustafa", "yas": 55},
    {"isim": "Ayten", "yas": 70},
    {"isim": "Hüseyin", "yas": 62},
    {"isim": "Fatma", "yas": 58},
    {"isim": "Aliye", "yas": 80},
    {"isim": "Kemal", "yas": 67},
    {"isim": "Cemal", "yas": 52},
    {"isim": "Asım", "yas": 75},
    {"isim": "Melahat", "yas": 61},
]

liste2 = [
    {"isim": "Alp", "yas": 19},
    {"isim": "Burak", "yas": 22},
    {"isim": "Zeynep", "yas": 18},
    {"isim": "Cem", "yas": 25},
    {"isim": "Aslı", "yas": 16},
    {"isim": "Deniz", "yas": 21},
    {"isim": "Emre", "yas": 17},
    {"isim": "Aleyna", "yas": 24},
    {"isim": "Mert", "yas": 29},
    {"isim": "Arda", "yas": 15},
]

sonuc = esnek_veri_filtresi(liste1, liste2, min_yas=20, bas_harf=("a", "A"))
print("Filtrelenmiş Veriler2", *sonuc)
