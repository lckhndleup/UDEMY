"""Proje 3
https://www.doviz.com/ sitesinden anlık olarak doların,euronun,altının ve borsanın değerlerini öğrenin ve
bunları kullanarak bir proje geliştirmeye çalışın.

Not: Bu projeyi, requests ve beautifulsoup kullanarak geliştirin."""

import requests

from bs4 import BeautifulSoup

url="https://kur.doviz.com"
response=requests.get(url)

html_icerigi=response.content

soup=BeautifulSoup(html_icerigi,"html.parser")

soup.prettify()

doviz_isimleri=soup.find_all("span",{"class":"name"})
doviz_degeri=soup.find_all("span",{"class":"value"})


"""for i in soup.find_all("span",{"class":"value"}):
    print(i)
    print("*********")"""
#print(len(doviz_degeri))
#print(len(doviz_isimleri))

for doviz,deger in zip(doviz_isimleri,doviz_degeri):
    #print("döviz ismi:",doviz.text)
    #print("döviz değeri:",deger.text)
    #print("**********************")
    doviz=doviz.text
    deger=deger.text
    doviz=doviz.strip()
    deger=deger.strip()
    doviz=doviz.replace("\n","")
    deger=deger.replace("\n","")


    a=input("görmek istediğiniz dövizin ismini giriniz:")
    """if doviz=="GRAM ALTIN":
        print("{} : {}".format(doviz,deger))

    elif doviz=="DOLAR":
        print("{} : {}".format(doviz,deger))
    elif doviz=="EURO":
        print("{} : {}".format(doviz,deger))"""
    if str(a)==doviz:
        print("{} {}".format(doviz,deger))
    
























