import re


with open("lvl1_bozuk_veri.txt", "r") as file:
    text = file.read()

    # telefon numarası paternleri oluşturup bir diziye ata
    # tel_patern = r"(?<!\d)(?:\+\d{1,3}|0)[\d\s\-\(\)]{9,20}\b"
    paternler = [
        r"(?<!\d)(?:\+90|0)[1-9]\d{2}[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{2}[\s\-\(\)]*\d{2}\b",  #  +90 veya 05...
        r"(?<!\d)[1-9]\d{2}[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{2}[\s\-\(\)]*\d{2}\b",  #  544...
        r"(?:\+\d{1,3})[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{4}\b",  # uluslararası (+1...)
    ]

    tel_ham = []
    for p in paternler:
        bulunanlar = re.findall(p, text)
        tel_ham.extend(bulunanlar)
    tel_temiz = []
    for t in tel_ham:
        sadece_rakamlar = "".join(filter(str.isdigit, t))
        if 10 <= len(sadece_rakamlar) <= 15:
            tel_temiz.append(t.strip())

    print(tel_ham)
    print("-" * 20)
    print(tel_temiz)

    # eposta oluşturup başka bir diziye ata

    post_patern = r"\S+@[\w.-]+\.[a-zA-Z]{2,}"
    mailler_ham = re.findall(post_patern, text)
    mailler_temiz = [m.strip(".,!?;:") for m in mailler_ham]
    print(mailler_ham)
    print("-" * 20)
    print(mailler_temiz)

    with open("lvl1_temiz_rehber.txt", "w", newline="") as file:
        file.write("temiz mailler\n")
        file.write("-----------------------------\n")
        for mail in mailler_temiz:
            file.write(mail + "\n")
        file.write("-----------------------------\n")
        file.write("temiz telefonlar\n")
        file.write("-----------------------------\n")
        for tel in tel_temiz:
            file.write(tel + "\n")
        file.write("-----------------------------\n")
