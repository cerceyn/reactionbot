from email import message
from multiprocessing.connection import Client
from random import randint,random,choice
from pyrogram.errors import (
    FloodWait, ApiIdInvalid,
)
from pyrogram import Client as PyrogramClient
from . import *
import sys
userbot=None
mainuserbot=None

dosya=""
api_id=""
api_hash=""

calinacakgrup=""

Clients= []

def hesaplariolustur ():
    global mainuserbot,dosya
    bilgi("( ! ) Hesaplar yerel bir değişkinene atanıyor...")
    mainmi = False
    dizin = soru("Hesapların olduğu dosyanın dizini:")
    if not dizin.endswith(".txt"):
        dizin += "\\hesaplar.txt"
    with open(dizin,"r") as file:
        dosya = file.read()
        dosya = dosya.split("\n")
    for i in dosya:
        ii = i.split("|")
        
        stringsession=""
        try:
            api_id = ii[0]
            api_hash= ii[1]
            stringsession = ii[2]
        except IndexError:
            hata("Hesapların olduğu dosya biçimi hatalı ! Lütfen hesapları tek satırda bir hesap olmak üzere şu formatta kaydedin:\nFormat: api_id|api_hash|string\nÖrnek:1636343|6sasn776askdghd3728|1JKgxqaıuq74294762hjcgajdgddeqhdqkhqdkdkkw=")
        
        if mainmi:
            try:
                mainmi= bool(ii[3])
            except IndexError:
                mainmi = None
                if i == 0:
                    mainmi = True
            except Exception:
                mainmi = None
        
        if mainmi == True and mainuserbot==None:
            try:
                mainuserbot = PyrogramClient(
                "cerceynbot_" + str(randint(1,1000)),
                api_id,
                api_hash,
                session_string=stringsession,
                device_model='Mac',
                system_version=' | Powered by @cerceyn',
                app_version=str('| 1.0'),
                in_memory=False)
                basarili(api_hash + " için main client oluşturuldu !")
            except FloodWait as e:
                hata(api_hash + f" için main client oluşturulamadı ! 🛑 Floodwait: {e.x}")
            except ApiIdInvalid:
                hata(api_hash + f" için main client oluşturulamadı ! 🛑 Api Id veya Hash Hatalı!")


        try:
            userbot = PyrogramClient(
            "cerceynbot_" + str(randint(1,1000)),
            api_id,
            api_hash,
            session_string=stringsession,
            device_model='Mac',
            system_version=' | Powered by @cerceyn',
            app_version=str('| 1.0'),
            in_memory=False)
            Clients.append(userbot)
            basarili(api_hash + " için client oluşturuldu !")
        except FloodWait as e:
            noadded(api_hash + f" için client oluşturulamadı ! 🛑 Floodwait: {e.x}")
        except ApiIdInvalid:
            noadded(api_hash + f" için client oluşturulamadı ! 🛑 Api Id veya Hash Hatalı!")

basarilihesap=0
hatalihesap=0
def hesaplarabaglan():
    global basarilihesap,hatalihesap
    bilgi("( ! ) Yerele bağlı hesaplara bağlanıyor...")
    hesapno=0
    for userbotstart in Clients:
        api_hash = dosya[hesapno].split("|")[1]
        try:
            userbotstart.start()
            basarili(api_hash + "oturuma giriş yapıldı !")
            basarilihesap+=1
        except ConnectionError:
            try:
                userbotstart.disconnect()
                userbotstart.connect()
                basarili(api_hash + "oturuma giriş yapıldı !")
                basarilihesap+=1
            except Exception as e:
                noadded(api_hash + f"oturuma giriş yapılamadı ! 🛑 {str(e)}")
                
                Clients.pop(hesapno)
                hatalihesap+=1
        except Exception as e:
            noadded(api_hash + f"oturuma giriş yapılamadı ! 🛑 {str(e)}")
            Clients.pop(hesapno)
            hatalihesap+=1
        hesapno+=1
    bilgi(f"{basarilihesap} hesaba giriş yapıldı! Hatalı hesap sayısı : {hatalihesap}")

def disconn():
    global basarilihesap,hatalihesap
    bilgi("( ! ) Yerele bağlı hesaplardan çıkılıyor...")
    for userbotstart in Clients:
        try:
            userbotstart.stop()
        except ConnectionError:
            try:
                userbotstart.disconnect()
            except Exception as e:
                pass
        except Exception as e:
            pass


def ifade_at(app):
    #bilgi("burayagirdi")
    global chatid,messageid,reaction
    #app.send_message("me","test !!!!")
    #bilgi("simdiburayagirdi")
    app.send_reaction(chat_id=chatid,message_id=int(messageid),emoji=str(reaction))

def yorum_at(app):
    # Get the discussion message
    m = app.get_discussion_message(chatid, messageid)
    global chatid,messageid,yorum
    # Comment to the post by replying
    m.reply(yorum)


hedefpost=""
chat=None
yorum=""
chatid=0
messageid=0
islem=0
reactions=["❤️","👍","👎","😁","🎉","😱","🔥","👏","🤔","🤩","🥳","🤮","💩","😥","🤯"]
reaction=""
kackez=0
if __name__ == "__main__":
    logo(True)

    hesaplariolustur()
    hesaplarabaglan()
    #print(len(Clients))
    while True:
        if hedefpost=="":
            hedefpost=soru("İşlem yapılacak postun linki ?")
            if not hedefpost.startswith("http"):
                noadded("Lütfen https://t.me/webtekno/6943 buna benzer bir link girin.")
                hedefpost=""
                continue
            hedefpost = hedefpost.split("//")[1].split("/")
            if not (hedefpost[0] in ["t.me","telegram.me"]):
                noadded("Lütfen içinde t.me olan bir link girin.")
                hedefpost=""
                continue
            
            chatid=hedefpost[1]
            chat = Clients[0].get_chat(chatid)
            chatid=chat.id
            messageid= hedefpost[2]
            basarili("Chat: {}\nMessage: {}".format(chatid,messageid))
        if islem==0:
            islem = soru("İfade işlemi için : 1, Yorum işlemi için 2 yazın")
            try:
                islem= int(islem)
                if not islem in [1,2]:
                    noadded("Lütfen sadece 1 veya 2 girin !")
                    islem=0
                    continue
            except:
                noadded("Lütfen sadece 1 veya 2 girin !")
                islem=0
                continue
        if yorum=="" and islem == 1:
            yorum = str(soru("Yoruma ne yazayım ?"))
        if reaction=="" and islem == 2:
            reaction=soru("Hangi emojiyi atayım ?")
            if not (reaction in reactions):
                noadded("Lütfen geçerli bir ifade seçin!")
                continue
        if kackez == 0 and islem == 2:
            kackez=soru("Bu emojiyi kaç kez atayım ?")
            try:
                kackez= int(kackez)
            except:
                noadded("Lütfen bir sayı girin!")
                kackez=0
                continue
        if (islem == 2 and reaction!="" and hedefpost!="" and  kackez != 0) or (islem == 1 and yorum !=""):
            if islem==2:
                basarili("Emoji: {}\nKaç kez atılacak: {}".format(reaction,kackez))
            else:
                basarili("Yorum: {}".format(yorum))
            break
    hsp=0
    for i in range(0,int(kackez)):
        bilgi("Döngü başlıyor 1...")
        app = Clients[hsp]
        bilgi("Döngü başlıyor 2...")
        #api_hash = dosya[hsp].split("|")[1]
        #print("Client: "+api_hash)
        try:
            if islem==1:
                ifade_at(app=app)
            else:
                yorum_at(app=app)
            basarili("{} nolu hesap için işlem başarılı!".format(i))
        except IndexError:
            noadded("IndexError.")
            break
        except ConnectionError:
            try:
                app.disconnect()
            except:
                pass
            try:
                app.connect()
            except:
                pass
            try:
                islem(app)
            except:
                pass
        except Exception as e:
            noadded("Hata: "+str(e))
        hsp+=1
    disconn()
    bilgi("bitti")
