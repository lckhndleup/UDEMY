from datetime import datetime
import locale

şu_an=datetime.now() #şu anın zamanını ve tarihini gösterir

şu_an.year #sadece yılı aldık

şu_an.month #sadece ayı aldık

şu_an.minute #sadece dakikayı aldık

şu_an.microsecond #saniyeyi aldık

şu_an.hour #sadece saaati adlık

datetime.ctime(şu_an) #daha güzel göstermek için boyle yazabiliriz

datetime.strftime(şu_an,"%Y") #sadece yılı bu şekildede alabiliriz.aynı şekilde
#ay için=%B , gün için=%A ,saat için=%X , gün için=%D

datetime.strftime(şu_an,"%Y %B %D") #yıl ay gün şeklinde yazar


#bu yazımları türkçe yapmak için 'locale' modülümüz var .
#import locale yaparak türkçeye çevirebiliriz.


locale.setlocale(locale.LC_ALL,"tr_TR") #normalde hoacanın verdiği kodda hata çıktı türkçe yazdırmadı
#ben internetten tr_TR yazısının yazılması gerekitğini öğrendim "" tırnaklar arasını boş bırakmıcaz.
datetime.strftime(şu_an,"%Y %B %D")

şu_an=datetime.now()
saniye=datetime.timestamp(şu_an) #şu anı saniye olarak döner.programlamadaki zaman mantığı 1970den sonra saniyeyi ekleyerek gider.

şu_an2=datetime.fromtimestamp(saniye) #saniyeyi datetime objesine çevirdik

şu_an=datetime.fromtimestamp(0) #1970-01-01 02:00:00 yani milad gibi :)

tarih=datetime(2018,12,23)

şu_an=datetime.now()

fark=şu_an-tarih #iki tarih arasındaki farkı bulduk







