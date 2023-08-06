#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaz

# def yazdir(kelime, adet):
#     print(kelime * adet)
# kelime=input("Kelimeyi giriniz: ")
# sayi=int(input('Döngüyü belirleyiniz: '))
# yazdir(kelime + '\n', sayi)
############################
#kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonk

#gönderilen 2 sayı arasındaki tüm asal sayıları bulun

# def asalBul(sayi1, sayi2):
#     if sayi1==1 or sayi2==1:
#         print("1\n")
    
# sayi1=int(input('İlk sayiyi giriniz: '))
# sayi2=int(input('İkinci sayiyi giriniz: '))

############################

#kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür
def bolenBul(number):
    for i in number:
        if number%i==0:
            print(i +'\n')


number=int(input("Sayıyı giriniz: "))
bolenBul(number)