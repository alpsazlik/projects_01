import json
import datetime

class FinansYoneticisi:
    def __init__(self):
        self.veri_dosyasi = "finans_verileri.json"
        self.veriler = self.verileri_yukle()

    def verileri_yukle(self):
        try:
            with open(self.veri_dosyasi, 'r') as dosya:
                return json.load(dosya)
        except FileNotFoundError:
            return {"Gelirler": [], "Giderler": []}

    def verileri_kaydet(self):
        with open(self.veri_dosyasi, 'w') as dosya:
            json.dump(self.veriler, dosya, indent=4)

    def gelir_ekle(self, miktar, aciklama, kategori="Diğer"):
        gelir = {
            "miktar": miktar,
            "aciklama": aciklama,
            "kategori": kategori,
            "tarih": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.veriler["Gelirler"].append(gelir)
        self.verileri_kaydet()
        print(f"Gelir Eklendi: {aciklama} - {miktar}")

    def gider_ekle(self, miktar, aciklama, kategori="Diğer"):
        gider = {
            "miktar": miktar,
            "aciklama": aciklama,
            "kategori": kategori,
            "tarih": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.veriler["Giderler"].append(gider)
        self.verileri_kaydet()
        print(f"Gider Eklendi: {aciklama} - {miktar}")

    def bakiye_goster(self):
        toplam_gelir = sum(gelir["miktar"] for gelir in self.veriler["Gelirler"])
        toplam_gider = sum(gider["miktar"] for gider in self.veriler["Giderler"])
        bakiye = toplam_gelir - toplam_gider
        print(f"\nFinansal Durum")
        print(f"Toplam Gelir: {toplam_gelir}")
        print(f"Toplam Gider: {toplam_gider}")
        print(f"Bakiye: {bakiye}")

        return bakiye

    def gelirleri_listele(self):
        if not self.veriler["Gelirler"]:
            print("Henüz gelir kaydı yok")
            return

        print("\nGelirler:")
        for i, gelir in enumerate(self.veriler["Gelirler"], 1):
            print(f"{i}. {gelir['aciklama']} - {gelir['miktar']} - {gelir['kategori']} - {gelir['tarih']}")

    def giderleri_listele(self):
        if not self.veriler["Giderler"]:
            print("Henüz gider kaydı yok")
            return

        print("\nGiderler:")
        for i, gider in enumerate(self.veriler["Giderler"], 1):
            print(f"{i}. {gider['aciklama']} - {gider['miktar']} - {gider['kategori']} - {gider['tarih']}")

def main():
    finans = FinansYoneticisi()
    while True:
        print("\nKişisel Finans Yöneticisi")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Bakiye Göster")
        print("4. Gelirleri Listele")
        print("5. Giderleri Listele")
        print("6. Çıkış")

        secim = input("\nSeçiminiz (1-6): ")

        if secim == "1":
            try:
                miktar = float(input("Gelir miktarı: "))
                aciklama = input("Açıklama: ")
                kategori = input("Kategori: ")
                finans.gelir_ekle(miktar, aciklama, kategori)
            except ValueError:
                print("Geçerli bir sayı girin.")

        elif secim == "2":
            try:
                miktar = float(input("Gider miktarı: "))
                aciklama = input("Açıklama: ")
                kategori = input("Kategori: ")
                finans.gider_ekle(miktar, aciklama, kategori)
            except ValueError:
                print("Geçerli bir sayı girin.")

        elif secim == "3":
            finans.bakiye_goster()

        elif secim == "4":
            finans.gelirleri_listele()

        elif secim == "5":
            finans.giderleri_listele()

        elif secim == "6":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen 1-6 arası bir sayı girin.")

if __name__ == "__main__":
    main()

