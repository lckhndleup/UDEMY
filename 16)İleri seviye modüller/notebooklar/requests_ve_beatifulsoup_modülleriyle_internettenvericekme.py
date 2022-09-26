import requests

from bs4 import BeautifulSoup

"""url="https://yellowpages.com.tr/ara?q=ankara" #url yi url değişkenine atadık.











response=requests.get(url)#request(get) ile tüm verileri çekicez

#print(response) #web sayfasının bilgilerini çekip çekmediğimizi kontrol ediyoruz.



html_icerigi=response.content

#html içeriğini daha iyi göstermek için beatifulsoup u kullanıcaz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


print(soup.prettify()) # Daha güzel bir görüntü için prettify() fonksiyonunu kullanıyoruz."""



url =  "https://yellowpages.com.tr/ara?q=Erkek+Giyim" # Site linkimiz

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


#print(soup.find_all("a")) # Bize tüm <a> etiketlerini liste şeklinde dönüyor.

for i in soup.find_all("a"):
    print(i.get("href"))
    print("*******************")



