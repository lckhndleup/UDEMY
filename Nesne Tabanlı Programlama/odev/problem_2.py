"""
Proje 2
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
"""
import time
import random
class Bilgisayar():
    def __init__(self,isim="apple",model="macbook",yaş=1,ram="8gb",fiyat=10000,işlemci="m1",kullanıcı="mehmetali"):
        self.isim=isim
        self.model=model
        self.yaş=yaş
        self.ram=ram
        self.fiyat=fiyat
        self.işlemci=işlemci
        self.kullanıcı=kullanıcı

    def model_degis(self):
        model_liste=["casper","dell","intel","huawei","sony","samsung","monster","hp"]
        b=1
        for i in model_liste:
            print(b,")",i)
            b+=1
        seçim=int(input("istediğiniz modelin numarasını giriniz:"))

        if seçim>0 and seçim<9:
            self.model=model_liste[seçim-1]
            print("model güncellendi:",self.model)
        if seçim>8 or seçim<0:
            print("yanlış giriş yapıldı...")
            return False



    def fiyat_artır(self):
        while True:
            fiyat_degis=input("fiyat artırmak için :'>'\nazaltmak için :'<'\nçıkış için:'q'ya basınız..")
            if fiyat_degis=="q":
                print("çıkış yapılıyor..")
                break
            elif fiyat_degis==">":
                artır=int(input("artırılacak miktarı giriniz:"))
                print("fiyat değiştiriliyor..")
                time.sleep(1)
                self.fiyat+=artır
                print("fiyat güncellendi :",self.fiyat)
            elif fiyat_degis=="<":
                azalt=int(input("azaltılacak miktarı giriniz:"))
                print("fiyat azaltılıyor...")
                time.sleep(1)
                self.fiyat-=azalt
                print("fiyat güncellendi:",self.fiyat)
            else:
                print("yanlış giriş çıkış yapılıyor..")
                break
    def ram_değiş(self):
        ram_liste=["8gb","16gb","32gb","64gb","128gb","256gb","512gb"]
        a=0
        for i in ram_liste:
            print(a,"nci seçenek=",i)
            a+=1
        seçim=int(input("değiştirmek istediğiniz numarayı giriniz:"))

        self.ram=ram_liste[seçim]
        print("ram güncelleniyor..")
        time.sleep(0.5)
        print("ram güncellendi..:",self.ram)

    def kullanıcı_degis(self,degissin_mi="bilgi yok"):
        while True:
            degissin_mi=input("Kullanıcı değiştirmek istiyorsanız '2'\nsabit kalması için '1' ye basın\nçıkmak için herhangi bir tuşa basın")
            if degissin_mi == "1":
                print("kullanıcı ismi:",self.kullanıcı)
                break

            elif degissin_mi == "2":
                yeni_kullanıcı = input("yeni kullanıcı ismini giriniz:")
                time.sleep(1)
                self.kullanıcı = yeni_kullanıcı
                print("kullanıcı güncellendi...:",self.kullanıcı)
                break
            else:
                print(".Bilgiler güncellendi...",self.kullanıcı,"çıkış yapılıyor...")
                break
    def yaş_değiş(self,yaş=0):
        yaş=int(input("Artırılacak yaşı giriniz:"))
        self.yaş+=yaş
        print("yeni yaşı:",self.yaş)


    def __str__(self):
        return "Bilgisayar ismi:{}\nModel:{}\nYaş:{}\nRam:{}\nFiyat:{}\nİşlemci:{}\nKullanıcı:{}".format(self.isim,self.model,self.yaş,self.ram,self.fiyat,self.işlemci,self.kullanıcı)












bilgisayar=Bilgisayar()

print("""
Bilgisayar sınıfı:
1)Bilgisayar Bilgilerini göster
2)fiyat artır
3)ram boyunu değiştir
4)kullanıcı değiştir
5)yaş değiştirme
6)model değiştirme
""")

while True:
    işlem=input("işlem:")
    if işlem=="1":
        print(bilgisayar)
    elif işlem=="2":
        bilgisayar.fiyat_artır()
    elif işlem=="3":
        bilgisayar.ram_değiş()
    elif işlem=="4":
        bilgisayar.kullanıcı_degis()
    elif işlem=="5":
        bilgisayar.yaş_değiş()
    elif işlem=="6":
        bilgisayar.model_degis()

