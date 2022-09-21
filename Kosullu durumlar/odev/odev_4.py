"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak
istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan
bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan
bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor"
şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs()
 fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""

cevap=input("üçgenin mi yoksa dörtgenin mi tipini bulmak istersiniz:")

if cevap=="dörtgen":
    kenar1=float(input("birinci kenar:"))
    kenar2=float(input("ikinci kenar:"))
    kenar3=float(input("üçüncü kenar:"))
    kenar4=float(input("dördüncü kenar:"))
    if kenar1==kenar2==kenar3==kenar4:
        print("kare")
    elif kenar1==kenar2 and kenar3==kenar4:
        print("dikdörtgen")
    elif kenar1==kenar3 and kenar2==kenar4:
        print("dikdörtgen")
    elif kenar1==kenar4 and kenar2==kenar3:
        print("dikdörtgen")
    else:
        print("sıradan")
elif cevap=="üçgen":
    kenar_1=float(input("birinci kenar:"))
    kenar_2=float(input("ikinci kenar:"))
    kenar_3=float(input("üçüncü kenar:"))
    if abs(kenar_1-kenar_2)<kenar_3<kenar_1+kenar_2 and abs(kenar_1-kenar_3)<kenar_2<kenar_1+kenar_3 and abs(kenar_2-kenar_3)<kenar_1<kenar_3+kenar_2:
        if kenar_3 == kenar_2 == kenar_1:
            print("eşkenar üçgen")
        elif kenar_1==kenar_2 or kenar_1==kenar_3 or kenar_2==kenar_3:
            print("ikizkenar üçgen")

        else:
            print("sıradan üçgen")
    else:
        print("üçgen belirtmiyor!!!")
