import random

def kelime_oyunu():
    kelime_listesi = ["FENERBAHCE", "SEN", "COK", "YASA"]

    secilen_kelime = random.choice(kelime_listesi)

    kalan_hak = 3


    bulunacak_kelime = ["_"] * len(secilen_kelime)

    print("Oyun Başladı")

    while kalan_hak > 0:
        print(" ".join(bulunacak_kelime))
        print(f"Kalan Hak: {kalan_hak}")

        tahmin = input("Bir harf girin ").upper()
        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Bir harf girilebilir")
            continue

        if tahmin in secilen_kelime:
            print("Doğru harf")
            for i in range(len(secilen_kelime)):
                if secilen_kelime [i] == tahmin:
                    bulunacak_kelime [i] = tahmin
                #Doğru harf girildi şimdi _ işareti doğru harf ile replace edilmeli

        else:
                #kullanıcının haklarından bir hakkını eksilt (-1) ile
            kalan_hak -= 1
            print(f"Yanlış harf. Kalan hak: {kalan_hak}")

                #AMA DÖNGÜ DEVAM ETTİKÇE KALAN HAK SIFIRLANIYOR NEDEN??

        if "_" not in bulunacak_kelime:
            print(" ".join(bulunacak_kelime))
            print("Kelşme bulundu")
            break

    if kalan_hak <= 0:
        print("Kaybettin")


kelime_oyunu()

