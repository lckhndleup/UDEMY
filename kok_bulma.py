"""
2nci dereceden bir bilinmeyenli denklemin köklerini bulma
denklem :ax^2+bx+c
delta:b^2-4ac
kökler:-b+-delta**0.5/(2*a)
"""
print("ikinci dereceden bir bilinmeyenli denklem programı...")
a=int(input("a yı gir:")) #int girmezsen string değer alır.
b=int(input("b yi gir:"))
c=int(input("c yi gir:"))
delta=(b**2)-(4*a*c)

birinci_kok=(-b+delta**0.5)/(2*a)
ikinci_kok=(-b-delta**0.5)/(2*a)
print("birinci kök: {}\nikinci kök:{}\n".format(birinci_kok,ikinci_kok))