import re
from collections import Counter
import string


class MetinAnaliz:
    def __init__(self, metin):
        self.metin = metin
        self.temiz_metin = self._temizle_metin()

    def _temizle_metin(self):
        temiz = self.metin.lower()
        temiz = re.sub(r'[^\w\s]', '', temiz)
        return temiz

    def istatistikler(self):
        kelimeler = self.temiz_metin.split()
        karakter_sayisi = len(self.metin)
        kelime_sayisi = len(kelimeler)

        ortalama_kelime_uzunlugu = sum(len(kelime) for kelime in kelimeler) / kelime_sayisi

        cumle_sayisi = len(re.split(r'[.!?]+', self.metin))

        return {
            'toplam_karakter': karakter_sayisi,
            'toplam_kelime': kelime_sayisi,
            'toplam_cumle': cumle_sayisi,
            'ortalama_kelime_uzunlugu': ortalama_kelime_uzunlugu
        }

    def kelime_frekanslari(self, n=10):
        kelimeler = self.temiz_metin.split()

        stop_words = {'ve', 'veya', 'bir', 'ama', 'için'}
        filtrelenmis = [kelime for kelime in kelimeler if kelime not in stop_words]

        frekanslar = Counter(filtrelenmis)
        return frekanslar.most_common(n)

    def ozet_cikar(self, max_kelime=20):
        kelimeler = self.temiz_metin.split()

        if len(kelimeler) <= max_kelime:
            return self.metin

        ozet = ' '.join(kelimeler[:max_kelime])
        return ozet + '...'

    def kelime_arama(self, aranan_kelime):
        kelimeler = self.temiz_metin.split()

        eslesmeler = [i for i, kelime in enumerate(kelimeler) if kelime == aranan_kelime]
        return eslesmeler


def test_analiz():
    ornek_metin = """
Yüz yıl önce doğdu şanlı efsane, yüz yaşında mutlu ol Fenerbahçe,
Yüz yıl önce doğdu şanlı efsane , yüz yaşında mutlu ol Fenerbahçe.
    """

    analiz = MetinAnaliz(ornek_metin)

    print("=== METİN İSTATİSTİKLERİ ===")
    stats = analiz.istatistikler()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n=== KELİME FREKANSLARI ===")
    frekanslar = analiz.kelime_frekanslari(5)
    for kelime, sayi in frekanslar:
        print(f"{kelime}: {sayi}")

    print("\n=== ÖZET ===")
    print(analiz.ozet_cikar(15))

    print("\n=== KELİME ARAMA ===")
    print("'python' kelimesi şu pozisyonlarda:", analiz.kelime_ara("Python"))


if __name__ == "__main__":
    test_analiz()