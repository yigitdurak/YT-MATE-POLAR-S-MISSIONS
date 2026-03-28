class Dedektif:
    def __init__(self):

        self.supheliler = ["Albay Mustard", "Profesör Plum", "Bayan Scarlet"]

    def supheli_ele(self, isim):

        if isim in self.supheliler:
            self.supheliler.remove(isim)
            print(f"[-] Kanıt bulundu: {isim} elendi.")
        else:
            print(f"[!] {isim} zaten listede yok veya daha önce elenmiş.")

    def suclu_kim(self):

        kalan_kisi = len(self.supheliler)

        if kalan_kisi == 1:

            print(f"Kesin bilgi, suçlu bulundu: {self.supheliler[0]}")
        elif kalan_kisi > 1:

            print("Henüz yeterli kanıt yok.")
        else:

            print("Mantık hatası: Herkes elendi!")


print("Olay Yeri İncelemesi Başlıyor...")
benim_dedektif = Dedektif()

benim_dedektif.suclu_kim()

benim_dedektif.supheli_ele("Profesör Plum")

benim_dedektif.suclu_kim()

benim_dedektif.supheli_ele("Albay Mustard")

benim_dedektif.suclu_kim()
