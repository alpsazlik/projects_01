import random

def kelime_oyunu():
    kelime_listesi = ["FENERBAHCE", "SEN", "COK", "YASA"];

    secilen_kelime = random.choice(kelime_listesi)

    kalan_hak = 3


    bulunacak_kelime = ("_") * len(secilen_kelime)

    print("Oyun Başladı")

    while True:
        print(" ".join(bulunacak_kelime))
        print(f"Kalan Hak: {kalan_hak}")

        tahmin = input("Bir harf girin ").upper()
        if len(tahmin) > 1:
            print("Bir harf girilebilir")
        else:
            if tahmin in secilen_kelime:
                print("Doğru harf")
                #Doğru harf girildi şimdi _ işareti doğru harf ile replace edilmeli

            else:
                #kullanıcının haklarından bir hakkını eksilt (-1) ile
                son_kalan_hak = kalan_hak-1

                #AMA DÖNGÜ DEVAM ETTİKÇE KALAN HAK SIFIRLANIYOR NEDEN??

                print(f"Yanlış harf. Kalan hak: {son_kalan_hak}")

                if '_' not in bulunacak_kelime:
                    print(" ".join(bulunacak_kelime))
                    print("Kelşme bulundu")
                    break
                if kalan_hak < 0:
                    print("Kaybettin")
                    break

kelime_oyunu()

