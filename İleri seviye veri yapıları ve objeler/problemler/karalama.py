class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi=file.read() #tüm dosyayı okuduk.

            kelimeler=dosya_icerigi.split()
            self.sade_kelimeler=list()
            for i in kelimeler:
                i=i.strip("")
                i=i.strip(",")
                i=i.strip(".")
                i=i.strip("\n")
                i=i.lower()

                self.sade_kelimeler.append(i)
    def tum_kelimeler(self):
        kelimeler_kumesi=set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)

        print("tüm kelimeler..........")
        for i in kelimeler_kumesi:
            print(i)

            print("***************************")
    def kelime_frekansı(self):
        kelime_sözlük=dict()

        for i in self.sade_kelimeler:
            if (i in kelime_sözlük):
                kelime_sözlük[i]+=1

            else:
                kelime_sözlük[i]=1
        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor".format(kelime,sayı))
            print("-------------------------------------")

    def kelime_varmı_yokmu(self):
        while True:

            cevap=input("Çıkmak için 'q' ya basın\nkelimeyi giriniz:")
            if cevap=="q":
                break
            else:
                for i in self.sade_kelimeler:
                    m=self.sade_kelimeler.count(cevap)
                    if cevap==i:
                        print("{} kelimesi {} defa geçmektedir".format(i,m))



















dosya=Dosya()
dosya.kelime_varmı_yokmu()