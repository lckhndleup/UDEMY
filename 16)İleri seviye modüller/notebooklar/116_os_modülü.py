#os modülü işletim sisteminde işlemler gerçekleştrirebildiğimiz standart bir python modulüdür.
import os
from datetime import datetime

os.getcwd() #dosyamızın nerde olduğunu görüyoruz

#dizini değiştirmek için os.chdir("dizinin yeni adresini yazarız")
#dizin altındaki tüm klasörleri görmek
os.listdir()
#bunun içerisnde for ile gezinelim
#for i in os.listdir():
    #print(i)

#bulunduğumuz dizinde klasör oluşturmak
#os.mkdir("deneme1")

#aynı anda 2 klasör oluşturmak

#os.makedirs("deneme2/deneme3")

#bir klasör altında bir klasörü silme

#os.rmdir("notebooklar/deneme1")
#bütün alt klasörleri silme: os.remodirs("a/b") a yı ve b yi siler

os.stat("ATATÜRK.jpg") #DOSYANIN özelliklerini gösteren bir veri yapısı döner

os.stat("ATATÜRK.jpg").st_mtime #bu dosyanın st_mtime ını  almak istedik saniye verdi

datetime.fromtimestamp(os.stat("ATATÜRK.jpg").st_mtime) #saniyeyi datetime objesine çevirdik


