"""
Proje 3
Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.
"""

class Hayvan():
    def __init__(self, büyüme="bilgi yok", beslenme="bilgi yok", hareket="bilgi yok", coğalma="bilgi yok",
                 solunum="bilgi yok", bosaltım="bilgi yok", tepki_verme="bilgi yok"):
        self.büyüme=büyüme
        self.beslenme=beslenme
        self.hareket=hareket
        self.cogalma=coğalma
        self.solunum=solunum
        self.bosaltım=bosaltım
        self.tepki_verme=tepki_verme
    def bilgileri_göster(self):
        pass


class Köpek(Hayvan):
    def __init__(self,büyüme="bilgi yok", beslenme="bilgi yok", hareket="bilgi yok", coğalma="bilgi yok",
                 solunum="bilgi yok", bosaltım="bilgi yok", tepki_verme="bilgi yok",tür="yok",kilo="yok",boy="yok",saldırma="yok",yaş=3):
        super().__init__(büyüme,beslenme,hareket, coğalma, solunum, bosaltım, tepki_verme)
        self.tür=tür
        self.kilo=kilo
        self.boy=boy
        self.saldırma=saldırma
        self.yaş=yaş

    def kilo_değiştir(self):

        while True:
            seçim=input("artır:'>'\nazalt:'<'\nçıkış:'herhangi bir tuş'")
            if seçim=="<":
                if self.kilo!=0:
                    self.kilo-=1
            elif seçim==">":
                if self.kilo!=100:
                    self.kilo+=1
            else:
                break

    def ortalama_ömür(self):
        print("köpek",self.yaş,"yaşındadır.Ortalama bir köpek ömrü 13 yıldır.")
        self.yaş=(13-self.yaş)
        print("ortalama kalan ömrü:")


    def __str__(self):
        return "Tür:{}\nKilo:{}\nBoy:{}\nSaldırma:{}\n".format(self.tür,self.kilo,self.boy,self.saldırma)
class Kuş(Hayvan):
    def __init__(self,büyüme="bilgi yok", beslenme="bilgi yok", hareket="bilgi yok", coğalma="bilgi yok",
                 solunum="bilgi yok", bosaltım="bilgi yok", tepki_verme="bilgi yok",tür="yok",yaşadığı_bölge="yok",kilo="yok",besin="--"):
        super().__init__(büyüme,beslenme, hareket, coğalma, solunum, bosaltım, tepki_verme)
        self.tür=tür
        self.yaşadığı_bölge=yaşadığı_bölge
        self.kilo=kilo
        self.besin=besin



class At(Hayvan):
    def __init__(self,büyüme="bilgi yok", beslenme="bilgi yok", hareket="bilgi yok", coğalma="bilgi yok",
                 solunum="bilgi yok", bosaltım="bilgi yok", tepki_verme="bilgi yok",hız="--",):
        super().__init__(büyüme, beslenme, hareket, coğalma, solunum, bosaltım, tepki_verme)
        self.hız=hız









