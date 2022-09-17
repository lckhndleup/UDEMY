"""
Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
"""
liste1=[]
for i in range (101):
    if i%3==0:
        liste1.append(i)
print(liste1)