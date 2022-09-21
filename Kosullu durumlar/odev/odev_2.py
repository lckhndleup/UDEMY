"""
Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""

sayı1=float(input("birinci sayı:"))
sayı2=float(input("ikinci sayı:"))
sayı3=float(input("üçüncü sayı:"))

if sayı1>=sayı2 and sayı1>=sayı3:
    print("en büyük sayı:",sayı1)
elif sayı2>=sayı1 and sayı2>=sayı3:
    print("en büyük sayı:",sayı2)
elif sayı3>=sayı1 and sayı3>=sayı2:
    print("en büyük sayı:",sayı3)
