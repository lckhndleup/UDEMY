"""Proje 1
Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede bulunduklarını ve isimlerini
ayrı ayrı "pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin."""
import os



"""/Users/mehmetali/Desktop/Kodlama Egzersizleri/16)İleri seviye modüller/problemler"""

print(os.walk("/Users/mehmetali"))

#for i in os.walk("/Users/mehmetali"):
    #print(i)

for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("/Users/mehmetali"):
    for i in dosya_isimleri:
        if (i.endswith(".txt")):
            print("txt dosyası------>>>>",i)
        elif(i.endswith(".pdf")):
            print("pdf dosyası------>>>>",i)
        elif(i.endswith(".mp4")):
            print("mp4 dosyası------>>>>",i)

