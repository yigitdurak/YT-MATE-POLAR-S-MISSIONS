# Roket Simülasyonu:


# Bir Roket sınıfı (class) oluşturun.
class Roket:
    # __init__ metodunu kullanarak bu roketin doğuştan gelen iki özelliği (attribute) olmasını sağlayın:
    # isim (örneğin "Apollo 11") ve yakit_seviyesi (başlangıçta tam sayı olarak verilecek).
    def __init__(self, isim, yakit):
        self.isim = isim
        self.yakit = yakit

    #   İçine yakit_doldur(miktar) adında bir metot yazın.
    #   Bu metot çalıştığında roketin mevcut yakıtına dışarıdan girilen miktar kadar ekleme yapsın
    #   ve "Yakıt eklendi. Yeni seviye: [..xx..]" yazdırsın.
    def yakitDoldur(self, ekYakit):
        self.yakit = self.yakit + ekYakit
        print(f"Yakit eklendi. Yeni seviye:{self.yakit}")

    #     İçine firlat() adında bir metot yazın. Bu metot çalıştığında:
    # Eğer yakit_seviyesi 10 ve üzerindeyse: Ekrana "Roket başarıyla fırlatıldı! 🌍 -> 🌕" yazdırsın
    # ve yakıt seviyesinden 10 birim düşsün.
    # Eğer yakit_seviyesi 10'dan azsa: Ekrana "Hata: Yetersiz yakıt! Lütfen yakıt doldurun." yazdırsın.

    def firlat(self):
        if self.yakit < 10:
            print("Hata: Yetersiz yakit! Lütfen yakit doldurun.")
        else:
            print("Roket başariyla firlatildi! 🌍 -> 🌕")
            self.yakit = self.yakit - 10
            print(self.yakit)


# Test: Kodun en altında bu sınıftan bir roket nesnesi üretin, yakıt doldurmayı ve fırlatmayı deneyerek kodunuzu test edin.
def main():
    benim_roketim = Roket("Apollo 11", 0)
    ekYakit = int(input("yakit ekle"))
    benim_roketim.yakitDoldur(ekYakit)
    benim_roketim.firlat()


if __name__ == "__main__":
    main()
