"""
Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
 Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
while True:
    sayı = int(input("sayı mukemmel mi?\nsayıyı giriniz:"))
    toplam = 0
    for i in range(1, sayı):
        if sayı % i == 0:
            toplam += i
    if toplam == sayı:
        print("-------------->>>>>>>>>>>>>>>mukemmel")
    else:
        print("-------------->>>>>>>>>>>>>>>mukemmmel değil")
