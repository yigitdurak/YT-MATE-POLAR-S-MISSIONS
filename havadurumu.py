import random


class HavaDurumu:
    def __init__(self):
        # ilk gunun havasi
        self.durum = "Güneşli"

    def yarin_ne_olacak(self):
        # bugune bakip yarini tahmin etme kismi random choices ile yuzdeleri ayarladik
        if self.durum == "Güneşli":
            self.durum = random.choices(["Güneşli", "Yağmurlu"], weights=[80, 20], k=1)[
                0
            ]
        elif self.durum == "Yağmurlu":
            self.durum = random.choices(["Güneşli", "Yağmurlu"], weights=[30, 70], k=1)[
                0
            ]


simulasyon = HavaDurumu()

sonuclar = []

for gun in range(1, 11):
    # gunun ekliyoruz
    sonuclar.append(f"{gun}. Gün: {simulasyon.durum}")
    # yarin icin
    simulasyon.yarin_ne_olacak()

print(", ".join(sonuclar) + "...")
