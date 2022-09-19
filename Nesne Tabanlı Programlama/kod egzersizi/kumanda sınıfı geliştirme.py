import random
import time

class Kumanda():
    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["trt"],kanal="trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if self.tv_durum=="kapalı":
            self.tv_durum="açık"
            print("televizyon açılıyor...")
        elif self.tv_durum=="açık":
            print("televizyon zaten açık...")
    def tv_kapat(self):
        if self.tv_durum=="kapalı":
            print("televizyon zaten kapalı..")
        else:
            print("televizyon kapanıyor...")
            self.tv_durum="kapalı"
    def ses_ayarları(self):
        while True:
            ses=input("sesi azaltmak için '<'\nsesi artırmak için '>'\nÇıkmak için 'çıkış' yazınız..")
            if ses=="<":
                if (self.tv_ses!=0):
                    self.tv_ses-=1
                print("ses:",self.tv_ses)
            elif ses==">":
                if self.tv_ses!=31:
                    self.tv_ses+=1
                print("ses:",self.tv_ses)
            else:
                print("Ses güncellendi:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor...")
        self.kanal_listesi.append(kanal_ismi)
        time.sleep(1)
        print("kanal eklendi..")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        print("şu anki kanal:",self.kanal_listesi[rastgele])
        self.kanal=self.kanal_listesi[rastgele]

    def __len__(self):
        return len(self.kanal_listesi)


    def __str__(self):
        return "tv durum:{}\ntv ses:{}\nKanal listesi:{}\nŞu anki Kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda=Kumanda()

print("""
Televizyon uygulaması:
1)Tv aç
2)Tv kapat
3)Ses ayarları
4)Kanal ekle
5)Kanal sayısını öğrenme
6)Rastgele kanala geçme
7)Tv bilgileri
çıkmak için  'q'ya basınız
""")

while True:
    işlem=input("işlemi giriniz:")
    if işlem=="q":
        print("çıkış yapılıyor..")
        break
    elif işlem=="1":
        kumanda.tv_ac()

    elif işlem=="2":
        kumanda.tv_kapat()
    elif işlem=="3":
        kumanda.ses_ayarları()
    elif işlem=="4":
        eklenecekler=input("Lütfen eklemek istediğiniz kanalları aralarında ',' koyarak yazınız")

        liste=eklenecekler.split(',')

        for i in liste:
            kumanda.kanal_ekle(i)
    elif işlem=="5":
        print("toplam kanal sayısı:",len(kumanda))
    elif işlem=="6":
        kumanda.rastgele_kanal()
    elif işlem=="7":
        print(kumanda)
    else:
        time.sleep(1)
        print("yanlış giriş yapıldı...\nÇıkış yapılıyor...")
        break
