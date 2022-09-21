""""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık."""


kelime="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb".lower()


harfler=list()

for i in kelime:
    harfler.append(i)

harfler_sozluk=dict()

for i in harfler:
    if i in harfler_sozluk:
        harfler_sozluk[i]+=1
    else:
        harfler_sozluk[i]=1

for harf,sayı in harfler_sozluk.items():
    print("{} harfi :{} defa kullanılmıştır".format(harf,sayı))
    print("----------------------")


