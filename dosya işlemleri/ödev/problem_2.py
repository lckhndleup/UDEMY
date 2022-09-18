"""
Proje 2
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları
rastgele yerleştirin. Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3
farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //
"""




with open("Futbolcular.txt","r",encoding="utf-8") as file:
    Galatasaray=[]
    Fenerbahçe=[]
    Beşiktaş=[]
    for satır in file:
        satır=satır[:-1]
        liste=satır.split(",")
        isim=liste[0]
        takım=liste[1]
        if takım=="Galatasaray":
            Galatasaray.append(isim+"\n")
        elif takım=="Fenerbahçe":
            Fenerbahçe.append(isim+"\n")
        elif takım=="Beşiktaş":
            Beşiktaş.append(isim+"\n")

    with open("Galatasaray.txt","w",encoding="utf-8") as file2:
        for i in Galatasaray:
            file2.write(i)
    with open("Fenerbahçe.txt","w",encoding="utf-8") as file3:
        for i in Fenerbahçe:
            file3.write(i)
    with open("Beşiktaş.txt","w",encoding="utf-8") as file4:
        for i in Beşiktaş:
            file4.write(i)






















