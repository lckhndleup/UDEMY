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


for  i in soup.find_all("a"):
    #print(i.get("href"))
    print(i)
    print("**********************************")

#print(soup.find_all("span",{"class":"flag icon icon-usd"}))
