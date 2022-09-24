"""
Program 2
1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.
"""

def asal_sayılar():
    for i in range(1,1001):
        if (i>1):
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                yield i

for i in asal_sayılar():
    print(i)

for j in asal_sayılar():
    print(j)