print("oyuncu kaydetme programı")

#kullanıcıdan 3 tane inputla bilgi alıcaz

ad=input("oyuncunun adı:")
soyad=input("oyuncunun soyadı:")
takım=input("oyuncunun takımı")

#bunları bir listeye atalım

bilgiler=[ad,soyad,takım]
print("bilgiler kaydediliyor....")

print("oyuncu adı: {}  \noyuncunun soyadı:{}\noyuncunun takımı:{}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("bilgiler kaydedildi.....")