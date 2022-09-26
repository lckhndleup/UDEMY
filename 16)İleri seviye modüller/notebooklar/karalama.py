from PIL import Image,ImageFilter


image=Image.open("kuş.jpg")

image.rotate(90).save("kuş4.jpg" )

image.convert(mode="L").save("kuş5.jpg")


degistir=(960,600)

image.thumbnail(degistir)
 
image.save("kuş6.jpg")

image.filter(ImageFilter.GaussianBlur(7)).save("kuş7.jpg")

image2=Image.open("ATATÜRK.jpg")

kırpılıcak_alan=(340,0,950,600)

image2.crop(kırpılıcak_alan).save("yüz.jpg")