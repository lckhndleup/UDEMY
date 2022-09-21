"""
Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""

vize1=int(input("vize1:"))
vize2=int(input("vize2:"))
final=int(input("final:"))
ortalama=vize1*0.3+vize2*0.3+final*0.4
if ortalama>=90:
    print("aa")
elif ortalama>=85:
    print("ba")
elif ortalama>=80:
    print("bb")
elif ortalama>=75:
    print("cb")
elif ortalama>=70:
    print("cc")
elif ortalama>=65:
    print("dc")
elif ortalama>=60:
    print("dd")
elif ortalama>=55:
    print("fd")
else:
    print("ff")