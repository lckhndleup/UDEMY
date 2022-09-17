print("""*********************
faktöriyel bulma programı
çıkmak için 'q' ya basınız.
*********************""")

while True:
    sayı = input("faktöriyelini bulmak istediğiniz sayıyı giriniz:")
    if sayı == "q":
        print("çıkış yapılıyor..")
        break
    else:
        sayı=int(sayı)
        faktöriyel = 1
        for i in range(2, sayı + 1):
            faktöriyel *= i
        print("{} sayısının faktöriyeli:".format(sayı),faktöriyel)












