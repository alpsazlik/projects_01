urunler = []

# ##### urunler listesi uzunluğu - değerli olamaz, yani stokta en düşük değer 0 olmalıdır bu da stokta ürün yok anlamına gelir.
    ####INDEX hatasını bundan dolayı alıyorsun

    ## URUN LISTELEME DE NEDEN + 1 koyma ihtiyacı hissettin? (print(f"{i}. {u['ad']} - Fiyat: {u['fiyat']} TL - Stok: {u['stok']}")
#) bu satıra?



def urun_ekle():
    ad = input("Ürün adı: ")
    fiyat = int(input("Ürün fiyatı: "))
    stok = input("Stok adedi: ")

    if ad == "" or fiyat == "":
        print("Hata: Boş değer girilemez!")
    urun = {"ad": ad, "fiyat": fiyat, "stok": stok}
    urunler.append(urun)
    print(f"{ad} başarıyla eklendi")


def urunleri_listele():

    if len(urunler) <= 0:
        print("Hiç ürün yok")
        return
    for i in range(len(urunler)):
        u = urunler[i]
        print(f"{i}. {u['ad']} - Fiyat: {u['fiyat']} TL - Stok: {u['stok']}")


def urun_ara():
    arama = input("Aramak istediğiniz ürün adı: ")
    bulundu = False
    for u in urunler:
        if u["ad"] == arama.lower(): ## Burada listede ad olarak key değeri vermişsin ama isim arıyorsun?
            print(f"Bulundu: {u['ad']} - {u['fiyat']} TL - Stok: {u['stok']}")
            bulundu = True
    if bulundu == False:
        print("Ürün bulunanadı")


def stok_guncelle():
    urunleri_listele()
    secim = int(input("Stok güncellemek istediğiniz ürün numarasını girin: "))
    if secim > len(urunler):
        print("Geçersiz seçim")
        return
    yeni_stok = input("Yeni stok değeri: ")
    urunler[secim]["stoklar"] = yeni_stok ## listeye eklememişsin yeni değeri?
    print("Stok güncellendi")


def urun_sil():
    urunleri_listele()
    secim = input("Silmek istediğiniz ürün numarasını girin: ")
    if secim.isdigit() == False:
        print("Geçersiz giriş")
        return
    secim = int(secim)
    if secim >= len(urunler):
        print("Geçersiz seçim")
    else:
        silinen = urunler.pop(secim + 1)
        print(f"{silinen['ad']} silindi.")


def toplam_deger():
    toplam = 0
    for u in urunler:
        toplam += u["fiyat"] * u["stok"]
    print("Stoktaki ürünlerin toplam değeri: " + toplam + " TL")

## 6 numaralı seçim nerede?
def menu():
    while True:
        print("\n--- MARKET STOK TAKİP SİSTEMİ ---")
        print("1. Ürün Ekle")
        print("2. Ürünleri Listele")
        print("3. Ürün Ara")
        print("4. Stok Güncelle")
        print("5. Ürün Sil")
        print("6. Toplam Stok Değeri Hesapla")
        print("7. Çıkış")

        secim = input("Seçiminiz: ")
        ## burada 6 yok?
        if secim == "1":
            urun_ekle()
        elif secim == "2":
            urunleri_listele()
        elif secim == "3":
            urun_ara()
        elif secim == "4":
            stok_guncelle()
        elif secim == "5":
            urun_sil()
        elif secim == 7:
            print("Çıkış yapılıyor")
            break
        else:
            print("Geçersiz seçim")


menu()

