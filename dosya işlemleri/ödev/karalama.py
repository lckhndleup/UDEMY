













"""
Proje 1
Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek kalanları "kalanlar.txt"
dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.

"""




with open("/Users/mehmetali/Desktop/dosya.txt","r",encoding="utf-8")as file:
    geçenler_listesi=[]
    kalanlar_listesi=[]

    for satır in file:

        satır = satır[:-1]

        liste = satır.split(",")

        isim = liste[0]

        not1 = int(liste[1])

        not2 = int(liste[2])

        not3 = int(liste[3])

        son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)


        if(son_not>=55):
            durum="geçti"
            geçenler_listesi.append(isim+"------>"+durum+"\n")
        else:
            durum="kaldı"
            kalanlar_listesi.append(isim+"------>"+durum+"\n")




    with open("geçenler.txt","w",encoding="utf-8")as file2:

        for i in geçenler_listesi:
            file2.write(i)

    with open("kalanlar.txt","w",encoding="utf-8")as file3:

        for i in kalanlar_listesi:
            file3.write(i)


