"""
kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun

beden kitle indeksi:kilo/boy(m)*boy(m)
"""
print("programa hoşgeldiniz..")

boy=float(input("boyunuzu metre cinsinden giriniz:"))
kilo=float(input("kilonuzu giriniz:"))

kitle_endeksi=kilo/(boy*boy)
print("vucut kitle indeksiniz:{}".format(kitle_endeksi))
