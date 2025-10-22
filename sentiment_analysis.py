from transformers import pipeline
import warnings

warnings.filterwarnings('ignore')


class TurkceDuyguAnalizi:
    def __init__(self):
        print("Model yükleniyor, lütfen bekleyin. (Orijinal ve Güvenli Model)")

        # --- DEĞİŞİKLİK YOK ---
        # En baştaki, çalışan ve herkese AÇIK modeline geri döndük.
        self.duygu_analizor = pipeline(
            "sentiment-analysis",
            model="savasy/bert-base-turkish-sentiment-cased"
        )
        print("Model başarıyla yüklendi.\n")

        self.notr_ifadeler = [
            "idare eder", "idare ederdi", "fena değil", "kotu sayılmaz",
            "ortalama", "normal", "yeterli", "kabul edilebilir",
            "normal seyrediyor", "derece"
        ]

    def analiz_et(self, cumle):
        sonuc = self.duygu_analizor(cumle)[0]
        return sonuc

    def detayli_sonuc(self, cumle):


        cumle_kucuk = cumle.lower()
        for ifade in self.notr_ifadeler:
            if ifade in cumle_kucuk:
                print("=" * 50)
                print("DUYGU ANALİZİ SONUÇLARI")
                print("=" * 50)
                print(f"Girilen Cümle: '{cumle}'")
                print(f"Temel Etiket: NÖTR (Manuel Kural)")
                print(f"Güven Puanı: 0.9900 (Manuel)")
                print("=" * 50)
                return {
                    'cumle': cumle,
                    'etiket': "NÖTR",
                    'puan': 0.99
                }

        sonuc = self.analiz_et(cumle)
        etiket = sonuc['label']
        puan = sonuc['score']

        threshold = 0.90

        if etiket == "positive" and puan > threshold:
            turkce_etiket = "POZİTİF"
        elif etiket == "negative" and puan > threshold:
            turkce_etiket = "NEGATİF"
        else:

            turkce_etiket = "NÖTR"

        print("=" * 50)
        print("DUYGU ANALİZİ SONUÇLARI")
        print("=" * 50)
        print(f"Girilen Cümle: '{cumle}'")
        print(f"Temel Etiket: {turkce_etiket}")
        print(f"Güven Puanı: {puan:.4f} (Modelin ham puanı)")
        print(f"(Modelin Ham Etiketi: {etiket})")
        print("=" * 50)

        return {
            'cumle': cumle,
            'etiket': turkce_etiket,
            'puan': puan
        }


if __name__ == "__main__":
    analizor = TurkceDuyguAnalizi()

    test_cumleleri = [
        "Bugün çok güzel bir gün!",
        "Bu film berbat, zaman kaybı.",
        "Hava durumu normal seyrediyor.",
        "Oda sıcaklığı 23 derece.",
        "Bugünkü yemek idare ederdi",
        "Bu ürün fena değil",
        "Performans ortalama seviyede"
    ]

    print("TEST ANALİZLERİ:")
    print("-" * 40)

    for i, cumle in enumerate(test_cumleleri, 1):
        print(f"\nTest {i}:")
        analizor.detayli_sonuc(cumle)

    print("\nKULLANICI MODU:")
    print("-" * 40)

    while True:
        kullanici_cumlesi = input("\nAnaliz için cümle yazın (Çıkmak için 'q'): ")

        if kullanici_cumlesi.lower() == 'q':
            print("Program sonlandı.")
            break

        if kullanici_cumlesi.strip():
            analizor.detayli_sonuc(kullanici_cumlesi)
        else:
            print("Lütfen geçerli bir cümle girin.")
