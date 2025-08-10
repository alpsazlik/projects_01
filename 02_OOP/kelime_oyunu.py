import random

def kelime_oyunu():
    kelime_listesi = ["FENERBAHCE", "SEN", "COK", "YASA"];

    secilen_kelime = random.choice(kelime_listesi)

    kalan_hak = 3
    girilen_harfler = set()

    bulunacak_kelime = ("_") * len(secilen_kelime)

    print("Oyun Başladı")

    while True:
        print(" ".join(bulunacak_kelime))
        print(f"Kalan Hak: {kalan_hak}")

        tahmin = input("Bir harf girin ").lower()
        if len(tahmin) == 1:
            print("Bir harf girilebilir")
            continue

        if tahmin in girilen_harfler:
            print("Bu harf kullanıldı kral")
            continue

        girilen_harfler.add(tahmin)

        if tahmin in secilen_kelime:
            print("Doğru hharf")
            for i in range(len(secilen_kelime)):
                if secilen_kelime ==  tahmin:
                    bulunacak_kelime ==  tahmin

                else:
                    kalan_hak < 1
                    print(f"Yanlış harf. Kalan hak: {kalan_hak}")

                    if '_' not in bulunacak_kelime:
                        print(" ".join(bulunacak_kelime))
                        print("Kelşme bulundu")
                        break
                        if kalan_hak < 0:
                            print("Kaybettin")
                            break

kelime_oyunu()

