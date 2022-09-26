import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "maliyildiz0307@gmail.com"

mesaj["To"] = "maliyildiz0307@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"


yazi = """

Smtp ile mail gönderiyorum..
mehmet ali yıldız
202151019010
akdeniz üniversitesi
elektrik elektronik mühendisi


"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("maliyildiz0307@gmail.com","27021991mali")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi....")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()







