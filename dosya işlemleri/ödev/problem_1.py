"""
Proje 1
Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek kalanları "kalanlar.txt"
dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.
"""

with open("dosya.txt","r",encoding="utf-8") as file5:
    gecenler = []
    kalanlar = []
    for satır in file5:

        satır=satır[:-1]
        liste=satır.split(",")
        isim=liste[0]
        not1=int(liste[1])
        not2=int(liste[2])
        not3=int(liste[3])
        son_not=not1*0.3+not2*0.3+not3*0.4

        if son_not>=55:
            durum="geçti"
            gecenler.append(isim+"---->"+durum+"\n")


        else:
            durum="kaldı"
            kalanlar.append(isim+"------>"+durum+"\n")


    with open("geçenler.txt","w",encoding="utf-8") as file6:
        for i in gecenler:
            file6.write(i)

    with open("kalanlar.txt","w",encoding="utf-8") as file7:
        for i in kalanlar:
            file7.write(i)











