while True:
    num_1=float(input("1.sayiyi girin:"))
    num_2=float(input("2.sayiyi girin:"))
    print("toplam:",num_1+num_2)
    print("fark:",num_1-num_2)
    print("carpim:",num_1*num_2)
    if num_2 !=0:
        print("Bölüm:",num_1/num_2)
    else:
        print("sıfıra bölünemez!")   
    bo=input("devam etmek istermisin y/n")
    if bo.lower()=="n":
        break
    else:
        continue