print("""*******************************************
ATM Programına hoşgeldiniz
İşlemler:
1)Bakiye Sorgulama

2)Para Yatırma

3)Para Çekme

Programdan çıkmak için 'q' ya basınız.
*******************************************
""")
sys_isim="mehmet ali"

hak=3
bakiye=0
while True:

  işlem=input("yapmak istediğiniz işlemi seçiniz:")
  if işlem == "q":
      print("çıkış yapılıyor..İyi günler Sayın {}".format(sys_isim), "bey")
      break

  elif işlem == "1":
      print("bakiyeniz:{}".format(bakiye))
  elif işlem == "2":
      miktar = int(input("yatırmak istediğiniz miktarı giriniz:"))
      bakiye += miktar
  elif işlem == "3":
      tutar = int(input("çekmek istediğiniz tutarı giriniz:"))
      if tutar <= bakiye:
          bakiye -= tutar
      else:
          print("bakiyeniz yetersiz..")

  else:
      print("geçersiz giriş yaptınız!!")







