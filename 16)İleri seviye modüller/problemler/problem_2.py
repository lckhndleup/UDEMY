"""Proje 2
Elinizde 5 kişinin maillerinin ve isimlerinin bulunduğu bir dosya olsun. Bu dosyayı okuyarak, her bir kişiye
isimleriyle beraber mail göndermeye çalışın. Dosya formatı şu şekilde olacak.

                       Mustafa Murat Coşkun,coskun.m.murat@gmail.com
                                       //
                                       //
                                       //
                                       //
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys
mesaj=MIMEMultipart()
mesaj["From"]="maliyildiz0307@gmail.com"
mesaj["To"]="maliyildiz0307@gmail.com"
mesaj["Subject"]="Smtp ile mail gönderme"

yazi="""

Smtp ile mail gönderiyorum..
mehmet ali yıldız
202151019010
akdeniz üniversitesi
elektrik elektronik mühendisi
"""
mesaj_gövdesi=MIMEText(yazi,"plain")
mesaj.attach(mesaj_gövdesi)

try:
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()

    mail.starttls()
    mail.login("maliyildiz0307@gmail.com","27021991mali")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("mail başarıyla gönderildi....")
    mail.close()
except:
    sys.stderr.write("bir sorun oluştu!!!")
    sys.stderr.flush()























