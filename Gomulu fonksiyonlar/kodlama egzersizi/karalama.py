"""def asal_mi(x):
    i=2
    if x==1:
        return False
    elif x==2:
        return True
    else:
        while(i<x):
            if (x%i ==0):
                return False
            i+=1
        return True
print(list(filter(asal_mi,range(1,100))))"""

"""liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]

i=0
yeni=list()

while (i<len(liste1) and len(liste2)):
    yeni.append(liste1[i],liste2[i]))
    i+=1
print(yeni)"""

"""liste=["elma","armut","muz","kiraz"]

i=0
yeni_liste=list()
for a in liste:
    yeni_liste.append((i,a))
    i+=1
print(yeni_liste)"""

"""def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
liste1=[True,True,False,True,False,True]
print(hepsi(liste1))"""

"""def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

liste1=[True,True,False,True,False,True]
liste2=[False,False,False,False,False,False]

print(herhangi(liste1))"""
def hepsi(liste):
    for i in liste:
        if not i :
            return False
    return True
liste1=[True,False,True,False,True]
print(hepsi(liste1))
































