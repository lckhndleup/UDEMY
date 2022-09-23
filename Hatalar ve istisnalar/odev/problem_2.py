
"""
Problem 2
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri
dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar
bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""

def cift_mi(sayı):
    if sayı%2==0:
        return sayı

    else:
        raise ValueError("sayı tek sayıdır")



liste=[2, 4, 6, 7, 9, 12, 13, 18, 31, 32, 34, 37, 49, 58, 68, 72, 233, 556, 2114, 6532]



for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        print("fonksiyon hata verdi")






