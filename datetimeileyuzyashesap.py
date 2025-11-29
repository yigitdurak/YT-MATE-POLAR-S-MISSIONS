import datetime
ad=input("adınız ne?\n")
yil=datetime.date.today().year
yas=int(input("yaşınızı giriniz:\n"))
yuzyasyili=100-yas
yuzegir=yil+yuzyasyili

print(f"Merhaba {ad}, şu an {yil} yılındayız.")
print(f"{yuzegir} yılında 100 yaşında olacaksın.")