while True:
    print(\n "Görev Takip Uygulaması")
    print("1.Görev Ekle")
    print("2. Görev Tamamla")
    print("3. Görev Sil")
    print("4. Görevleri Görüntüle")
    print("5 Çıkış Yap")

secim == input("Seçim: ")

if secim == "1":
    print("Görev Ekleme Seçildi")

elif secim == "2":
    print("Görev Tamamla")

elif secim == "3":
    print("Görev Silme Seçildi")

elif secim == "4":
    print("Görev Görüntüle Seçildi")

elif secim == "5":
    print("Çıkış Yap")
    break
else:
    print("Geçersiz Seçim Tekrar Deneyein")

gorevler = []
isim = input("Görev Adı: ")
gorevler.append({"isim": isim, "tamamlandi": False})
for i, gorev in enumerate(gorevler, 1):
    durum = "Başarılı" if gorev["tamamlandi"] else "Başarısız"
    print(f"{i}, {gorev["isim"]} {durum}")