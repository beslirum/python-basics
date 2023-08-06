'''
username = "Rumeysa"
password = "123"

isLoggedin = (username=="Rumeysa") and (password=="123")


"""if isLoggedin == True:
    print("Hoşgeldiniz.") # boşluk önemli"""
if (username=="Rumeysa"):
    if (password=="123"):
        print("Hosgeldiniz")
    else:
        print("parola yanlış")

else:
    print("Bilgide hata var")

#else if = elif
'''

num = int(input("sayi:"))
if num>0:
    print("sayı pozitif")
elif num==0:
    print("sayı sıfır")
else:
    print("sayı negatif")