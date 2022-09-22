"""
Problem 2
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen
belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

Not: filter() fonksiyonunu kullanmaya çalışın.
"""
liste1=[(3, 4, 5), (6, 8, 10), (3, 10, 7)]
def ücgen_mi(demet):
    if demet[0]+demet[1]>demet[2] and demet[2]+demet[1]>demet[0] and demet[2]+demet[0]>demet[1]:
        return demet[0],demet[1],demet[2]

print(list(filter(ücgen_mi,liste1)))