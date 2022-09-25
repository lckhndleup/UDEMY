"""
kullanıcıdan bir dik üçgenin dik olan iki kenarını (a,b)alın ve hipotenüs uzunluğunu bulmaya çalışın
a^2+b^2=c^2
"""
print("hipotenüs programına hoşgeldiniz..")

dik1=float(input("birinci dik kenarı giriniz:"))
dik2=float(input("ikinci dik kenarı giriniz:"))

hipotenus=(dik1**2+dik2**2)**0.5

print("hipotenus uzunluğu:{}".format(hipotenus))


