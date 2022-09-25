"""
kullanıcıdan aldığınız 3 tane sayıyı carparak ekrana yazdırın.ekrana yazdırma işlemini .format metoduyla yapmaya çalışın
"""

print("""*************************
        HOŞGELDİNİZ
*************************
""")

sayi1=int(input("1nci sayı:"))
sayi2=int(input("2nci sayı:"))
sayi3=int(input("3ncü sayı:"))
carpım=sayi1*sayi2*sayi3

print("{} x {} x {} = {} dir".format(sayi1,sayi2,sayi3,carpım))