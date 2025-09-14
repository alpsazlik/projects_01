import requests
from colorama import Fore, Style, init
import time



API_KEY = "9f4102bf15bced5c432ecc1df8481484"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def hava_durumu_sorgula(sehir):

    try:

        url = f"{BASE_URL}q={sehir}&appid={API_KEY}&units=metric&lang=tr"
        response = requests.get(url)
        veri = response.json()

        if veri["cod"] != "404":
            ana = veri["main"]
            sicaklik = ana["temp"]
            basinc = ana["pressure"]
            nem = ana["humidity"]
            hava = veri["weather"][0]
            aciklama = hava["description"].title()
            ruzgar = veri["wind"]["speed"]

            return {
                "sicaklik": sicaklik,
                "basinc": basinc,
                "nem": nem,
                "aciklama": aciklama,
                "ruzgar": ruzgar,
                "sehir": sehir.title()
            }
        else:
            return None

    except Exception as e:
        print(f"{Fore.RED}Hata oluştu: {e}")
        return None


def renkli_cizgi():
    print(f"{Fore.CYAN}{'═' * 40}")


def renkli_hava_durumu_goster(bilgiler):
    renkli_cizgi()
    print(f"{Fore.CYAN}  {bilgiler['sehir']} Hava Durumu")
    renkli_cizgi()

    if bilgiler["sicaklik"] > 30:
        sicaklik_renk = Fore.RED
    elif bilgiler["sicaklik"] > 20:
        sicaklik_renk = Fore.YELLOW
    else:
        sicaklik_renk = Fore.BLUE

    print(f"{Fore.WHITE}Sıcaklık: {sicaklik_renk}{bilgiler['sicaklik']}°C")
    print(f"{Fore.WHITE}Durum:    {Fore.BLUE}{bilgiler['aciklama']}")
    print(f"{Fore.WHITE}Nem:      {Fore.CYAN}{bilgiler['nem']}%")
    print(f"{Fore.WHITE}Rüzgar:   {Fore.WHITE}{bilgiler['ruzgar']} m/s")
    print(f"{Fore.WHITE}Basınç:   {Fore.WHITE}{bilgiler['basinc']} hPa")
    renkli_cizgi()


def sohbet_botu():
    print(f"{Fore.GREEN}Merhaba ben hava durumu botuyum.")
    time.sleep(1)
    print(f"{Fore.GREEN}Sana şehirlerin hava durumu hakkında bilgi verebilirim.")
    time.sleep(1)

    while True:
        print(f"\n{Fore.YELLOW}Bir şehir ismi yazabilirsin ")
        print(f"{Fore.YELLOW}Çıkmak için 'quit' yazabilirsin.")

        girdi = input(f"{Fore.WHITE}Sen: ").strip()

        if girdi.lower() in ['quit', 'exit', 'çıkış', 'bye', 'q']:
            print(f"{Fore.GREEN}Görüşmek üzere. İyi günler.")
            break

        if not girdi:
            print(f"{Fore.RED}Lütfen bir şehir ismi yaz.")
            continue

        print(f"{Fore.BLUE}Biraz bekleyin, {girdi.title()} için hava durumunu arıyorum...")
        time.sleep(1)

        hava_bilgisi = hava_durumu_sorgula(girdi)

        if hava_bilgisi:
            renkli_hava_durumu_goster(hava_bilgisi)

            if "yağmur" in hava_bilgisi["aciklama"].lower():
                print(f"{Fore.BLUE}  Yanına şemsiye almayı unutma")
            elif hava_bilgisi["sicaklik"] > 30:
                print(f"{Fore.RED} Çok sıcak! Bol su iç ve gölgede kal.")
            elif hava_bilgisi["sicaklik"] < 5:
                print(f"{Fore.BLUE}  Hava soğuk kalın giyin.")
            elif "güneş" in hava_bilgisi["aciklama"].lower():
                print(f"{Fore.YELLOW}️  Güneşli güzel bir gün keyfini çıkar.")

        else:
            print(f"{Fore.RED}Üzgünüm, '{girdi}' şehri bulunamadı veya bir hata oluştu.")
            print(f"{Fore.YELLOW}Lütfen şehir isminin doğru yazıldığından emin ol.")
            print(f"{Fore.YELLOW}İngilizce ismini yazmayı dene (ör: Istanbul, Ankara)")


sohbet_botu()