import asyncio,os, bs4
from pyrogram import Client
from pyrogram.errors import *
from rich.panel import Panel
from rich.console import Console
from random import choice, randint
import requests
from android import *

console = Console()

def logo (satirbırak=False):
    text = "█▀▀ █▀▀ █▀█ █▀▀ █▀▀ █▄█ █▄░█\n█▄▄ ██▄ █▀▄ █▄▄ ██▄ ░█░ █░▀█"
    if satirbırak:
        for i in range(25):
            print("\n")
        console.print(Panel(f'[bold cyan]{text}[/]',width=90),justify="center")
    else:
        console.print(Panel(f'[bold cyan]{text}[/]',width=90),justify="center")

Clients=[]
satir = ""
stringq = ""

API_ID = ""
API_HASH = ""
loop = asyncio.get_event_loop()
os.system("clear")

async def session_olustur():
    logo()
    API_ID = input("Telegram API ID: ")
    API_HASH = input("Telegram API HASH: ")
    async with Client("userbot", api_id=API_ID, api_hash=API_HASH) as app:
        print('\n\n')
        stringq = await app.export_session_string()
        print(stringq)
        print('\n')
    satir = "{}|{}|{}".format(API_ID,API_HASH,stringq)

    print(f"\n\nSatır: {satir}\n\n")
    with open("hesaplar.txt","a") as file:
        file.write(satir)


def main():
        numara = 0
        hh=0
        while hh<1:
            numara = soru(" Telefon Numaranız: ")
            if numara.startswith("+"):
                hh+=1
            else:
                noadded("(!) Geçersiz Bir Numara Girdiniz Örnekte Gibi Giriniz. Örnek: +90xxxxxxxxxx")
        try:
            rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
        except:
            hata("(!) Kod Gönderilemedi. Telefon Numaranızı Kontrol Ediniz.")
            exit(1)
      
        sifre = soru("(?) Telegram'dan Gelen Kodu Yazınız: ")
        try:
            cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
        except:
            hata("(!) Büyük İhtimal Kodu Yanlış Yazdınız. Lütfen Scripti Yeniden Başlatın.")
            exit(1)
        app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
        soup = bs4.BeautifulSoup(app, features="html.parser")

        if soup.title.string == "Create new application":
            bilgi("(i) Uygulamanız Yok. Oluşturuluyor...")
            hashh = soup.find("input", {"name": "hash"}).get("value")
            app_title = choice(["cer", "cerc", "tgc", "madelineproto", "telethon", "pyrogram"]) + choice(["user", "bt", "vue", "jsx", "python", "php"]) + choice(["", "_"]) + choice([str(randint(10000, 99999))])
            app_shortname = choice(["cercey", "cerceyn", "tg", "madelineproto", "telethon", "pyrogram"]) + choice(["user", "bt", "vue", "jsx", "python", "php"]) + choice(["", "_"]) + choice([str(randint(10000, 99999))])
            AppInfo = {
                "hash": hashh,
                "app_title": app_title,
                "app_shortname": app_shortname,
                "app_url": "",
                "app_platform": choice(["ios", "web", "desktop"]),
                "app_desc": choice(["madelineproto", "pyrogram", "telethon", "", "web", "cli"])
            }
            app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text

            if app == "ERROR":
                hata("(!) Telegram otomatik app açma işlemini blockladı. Scripti yeniden başladın./ Please restart!")
                exit(1)


            bilgi("(i) Uygulama başarıyla oluşturuldu")
            bilgi("(i) API ID/HASH alınıyor...")
            newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
            newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

            g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})

            try:
                app_id = g_inputs[0].string
                api_hash = g_inputs[1].string
            except IndexError:
                AppInfo = {
                    "hash": hashh,
                    "app_title": 'siribot',
                    "app_shortname": 'siribot',
                    "app_url": "",
                    "app_platform": choice(["android","ios", "web", "desktop"]),
                    "app_desc": choice(["madelineproto", "pyrogram", "telethon", "", "web", "cli"])
                }
                app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
                newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
                newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

                g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
                app_id = g_inputs[0].string
                api_hash = g_inputs[1].string

            bilgi("(i) Bilgiler Getirildi! İsterseniz bunları not edebilirsiniz.")
            onemli(f"API ID: {app_id}")
            onemli(f"API HASH: {api_hash}")
            bilgi("(i) String alınıyor...")

            return numara, app_id, api_hash
        elif soup.title.string == "App configuration":
            bilgi("(i) Halihazır da Uygulama Oluşturmuşsunuz. API ID/HASH Çekiliyor...")
            g_inputs = soup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
            app_id = g_inputs[0].string
            api_hash = g_inputs[1].string

            bilgi("(i) Bilgiler Getirildi! İsterseniz bunları not edebilirsiniz.")
            onemli(f"API ID: {app_id}")
            onemli(f"API HASH: {api_hash}")
            bilgi("(i) String alınıyor...")

            return numara, app_id, api_hash
        else:
            hata("(!) Bir Hata Oluştu.")



def TelegramClient():
    numara, app_id, api_hash = main()
    client = Client("userbot",
                api_id=app_id,
                api_hash=api_hash,
                phone_number=numara,
                device_model='Mac',
                system_version=' | Powered by @cerceyn',
                app_version=str('| 1.0'),
                in_memory=True)
    
    phone_code_hash = loop.run_until_complete(client.send_code(numara))
    code = soru("(?) Telegram'dan Gelen Kodu Yazınız: ")
    try:
        loop.run_until_complete(client.sign_in(numara,phone_code_hash.phone_code_hash,code))
    except SessionPasswordNeeded:
        ipucu = loop.run_until_complete(client.get_password_hint())
        fa = soru(f"(?) Hesabınızın İki Adımlı Doğrulama Şifresini Yazınız: \nİpucu: {ipucu}")
        try:
            loop.run_until_complete(client.check_password(fa))
        except BadRequest:
            hata("(!) 2 Aşamalı Şifrenizi Yanlış Yazdınız. Lütfen Tekrar Deneyiz. [Fazla Deneme Yapmak Ban Yemenize Neden Olur]")
    stringq = loop.run_until_complete(client.export_session_string())
    return stringq, app_id,api_hash




if __name__ == "__main__":
    logo(True)
    while True:
        stringq, app_id,api_hash = TelegramClient()
        satir = "{}|{}|{}".format(API_ID,API_HASH,stringq)
        print(f"\n\nSatır: {satir}\n\n")
        try:
            with open("hesaplar.txt","a") as file:
                file.write(satir)
        except:
            pass
        ss = input("\n\n\n[!] Başka bir hesap için string almak ister misiniz ? (y/n)")
        API_ID = ""
        API_HASH = ""
        if ss in ["y","Y"]:
            print("Güle güle!")
            break
