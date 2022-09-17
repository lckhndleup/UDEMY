"""
Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

while True:
    sayı = input("sayıyı giriniz:")

    liste = list(sayı)

    print("boyutu:", len(sayı))
    x = int(sayı)
    print(x)
    """if len(str(x)) == 4:
        bir = x % 10
        first = bir ** 4
        on = x % 10
        second = on ** 4
        yuz = x % 10
        thırd = yuz ** 4
        bin = x % 10
        fourth = bin ** 4
        toplam = first + second + thırd + fourth
        print(toplam)
    elif len(str(x))==3:
        bir = x % 10
        first = bir ** 4
        on = x % 10
        second = on ** 4
        yuz = x % 10
        thırd=yuz**4
        toplam = first + second + thırd
        print(toplam)"""




