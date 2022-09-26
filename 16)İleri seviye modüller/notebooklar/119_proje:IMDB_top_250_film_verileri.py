import requests

from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"

response=requests.get(url) #internetten veriyi aldık

html_icerigi=response.content #response un içinden bu web sayfasının kaynağını alıcaz

soup=BeautifulSoup(html_icerigi,"html.parser") #soup isimli Beatifulsoup objesi oluşturuyoruz

"""for i in soup.find_all("td",{"class":"titleColumn"}):
    print(i.text)
    print("**********************")""" #isim geçen yerleri alıyoruz.


basliklar=soup.find_all("td",{"class":"titleColumn"})#film isimlerinin listesini döner

ratingler=soup.find_all("td",{"class":"ratingColumn imdbRating"})#filmlerin ratinglerini döner

a=float(input("Ratingi giriniz:"))

for baslik,rating in zip(basliklar,ratingler):#zip iki listeyi birleştirip liste içinde demet oluşturuyor.
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n", "")

    rating = rating.strip()
    rating = rating.replace("\n", "")

    if(float(rating)>a):
        print("film ismi:{} filmin ratingi:{}".format(baslik,rating))










