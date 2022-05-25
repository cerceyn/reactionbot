import asyncio
from pyrogram import Client
from rich.panel import Panel
from rich.console import Console

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

if __name__ == "__main__":
    logo(True)
    while True:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(session_olustur())
        ss = input("\n\n\n[!] Başka bir hesap için string almak ister misiniz ? (y/n)")
        API_ID = ""
        API_HASH = ""
        if ss in ["y","Y"]:
            print("Güle güle!")
            break
