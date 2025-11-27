from bs4 import BeautifulSoup
import requests
import time
import smtplib

#kitap linki
url = "https://www.kitapyurdu.com/kitap/kan-ve-gul-bir-kara-dejavu/594741.html"

sender_mail = "mail_adresin@gmail.com"
sender_password = "mail_uygulama_sifresini_yaz"
receiver_mail = "mail_adresin@gmail.com"

#headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def send_mail(price):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) # gmail sunucusu
        server.ehlo() #handshake
        server.starttls() # bağlantıyı şifrele
        server.login(sender_mail, sender_password) # giriş 

        subject = "Fiyat Dustu!"
        body = f"Kitabinin fiyati dustu!\nYeni Fiyat: {price} TL\nLink: {url}"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(sender_mail, receiver_mail, msg)
        server.quit()

    except Exception as e:
        print(f"Mail atarken hata oluştu: {e}")


def price_finder():
    try:
        #html kodu çekiyoruz
        resource = requests.get(url, headers=headers)
        #bağlantı kontrolü
        if resource.status_code == 200:
            soup = BeautifulSoup(resource.content, "lxml")

            #fiyatın oldğu etiket
            price_element = soup.find(itemprop= "price")

            #fiyat
            price = float(price_element["content"])

            #fonksiyon fiyatı döndürüyor
            return price     
        else:
            print(f"Siteye erişilemedi. Hata kodu: {resource.status_code}")
    except Exception as e:
        print("Hata")
    return None

#referans fiyat alınıyor
old_price = price_finder()

while True:
    time.sleep(3600)

    updated_price = price_finder()

    #fiyat alınamazsa pas geç
    if updated_price is None:
        continue

    if updated_price > old_price:
        print(f"Fiyat yükseldi. Artış: {updated_price - old_price:.2f} TL.")
        old_price = updated_price #eski fiyatı bi sonrakine güncelliyoruz
    
    elif updated_price < old_price:
        print(f"Fiyat düştü. Düşüş: {old_price - updated_price:.2f} TL.")
        send_mail(updated_price) #mail gönder
        old_price = updated_price #eski fiyatı bi sonrakine güncelliyoruz
    
    else:
        pass
        #print(f"Değişiklik yok. ({updated_price} TL)")

