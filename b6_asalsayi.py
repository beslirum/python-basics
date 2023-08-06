sayi=int(input("Sayınızı giriniz: "))

asalMi= True

if sayi==1:
    asalMi=False
for i in range(2, sayi):
    if (sayi%i==0):
        asalMi=False
        break

if asalMi==True:
    print("Sayı Asaldır")
else:
    print("Sayı Asal Değildir.")