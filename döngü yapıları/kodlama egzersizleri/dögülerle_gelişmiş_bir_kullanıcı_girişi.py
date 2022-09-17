print("""
*************************
Kullanıcı girişi programı
*************************""")

sys_kullanıcı="mali"
sys_parola="12345"
hak=3
while True:
    kullanıcı=input("kullanıcı adınızı giriniz:")
    parola=input("şifrenizi girniz:")

    if hak==0:
        print("hakkınız bitti...Çıkış yapılıyor...")
        break
    elif hak>0:
        if kullanıcı != sys_kullanıcı and parola == sys_parola:
            print("kullanıcı adınızı yanlış girdiniz!kalan hakkınız:{}".format(hak))
            hak-=1
        elif kullanıcı == sys_kullanıcı and sys_parola != parola:
            print("parola yanlış girildi!Kalan hakkınız:{}".format(hak))
            hak-=1
        elif kullanıcı != sys_kullanıcı and parola != sys_parola:
            print("parola ve kullanıcı adı yanlış girildi!!Kalan hakkınız:{}".format(hak))
            hak-=1
        else:
            print("hoşgeldiniz...")
            break





