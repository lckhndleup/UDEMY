"""
Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""





for i in range (1,11):
    print("\n---{} LER TABLOSU--".format(i))
    for a in range(1,11):
        çarpım=a*i
        print("{}x{}={}".format(a,i,çarpım))


