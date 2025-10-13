import random
import string


def sifre_olustur(uzunluk=12):
    if uzunluk < 4
        print("Şifre en az 4 karakter olmalı!")
        return None

    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase
    rakamlar = string.digits
    ozel_karakterler = "!@#$%&*"

    sifre = []
    sifre.append(random.choice(kucuk_harfler))
    sifre.append(random.choice(buyuk_harfler))
    sifre.append(random.choice(rakamlar))
    sifre.append(random.choice(ozel_karakterler))

    tum_karakterler = kucuk_harfler + buyuk_harfler + rakamlar + ozel_karakterler

    for i in range(uzunluk - 4):
        sifre.append(random.choice(tum_karakterler))

    random.shuffle(sifre)
    return ''.join(sifre)


def sifre_guc_test(sifre):
    if not sifre
        return "Geçersiz şifre"

    puan = 0
    uzunluk_puani = 0

    if len(sifre) >= 12:
        uzunluk_puani = 2
    elif len(sifre) >= 8:
        uzunluk_puani = 1

    kucuk_harf_var = any(c.islower() for c in sifre)
    buyuk_harf_var = any(c.isupper() for c in sifre)
    rakam_var = any(c.isdigit() for c in sifre)
    ozel_karakter_var = any(c in "!@#$%&*" for c in sifre)

    puan = uzunluk_puani + kucuk_harf_var + buyuk_harf_var + rakam_var + ozel_karakter_var

    if puan >= 6:
        return "Güçlü"
    elif puan >= 4:
        return "Orta"
    else:
        return "Zayıf"


def sifre_kontrol(sifre):
    if len(sifre) < 6:
        return "Şifre çok kısa!"

    if sifre.lower() == "password":
        return "Çok basit şifre"

    if sifre == "123456":
        return "Bu şifre çok yaygın"

    return "Şifre uygun"


def main():
    print("Şifre Yöneticisi")

    while True:
        print("\n1. Güçlü Şifre Oluştur")
        print("2. Şifre Gücünü Test Et")
        print("3. Şifre Kontrol Et")
        print("4. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            try:
                uzunluk = int(input("Şifre uzunluğu (en az 4): "))
                sifre = sifre_olustur(uzunluk)
                if sifre:
                    guc = sifre_guc_test(sifre)
                    print(f"Oluşturulan şifre: {sifre}")
                    print(f"Güç seviyesi: {guc}")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

        elif secim == "2":
            sifre = input("Test edilecek şifre: ")
            guc = sifre_guc_test(sifre)
            print(f"Şifre gücü: {guc}")

        elif secim == "3":
            sifre = input("Kontrol edilecek şifre: ")
            sonuc = sifre_kontrol(sifre)
            print(f"Kontrol sonucu: {sonuc}")

        elif secim == "4":
            print("Görüşürüz")
            break

        else:
            print("Geçersiz seçim!")

    print("Program sonlandı")


if __name__ == "__main__":
    main()