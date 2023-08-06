'''
1-100 arasında rastgele üretilecel bir sayıyı aşağı yukarı ifadeleri ile
buldurmaya çalışın.
*** 100 üzerinden puanlama yapın her puan 20 puan
***Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
üzerinden hesaplansın
'''
import random
sayi = random.randint(1,100)

skor=100
hak = int(input("Hak sayısını giriniz."))
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    x=int(input("tahmininizi giriniz: "))
    if x==sayi:
        print(f"Tebrikler, {sayac} defada bildiniz")
    elif x>sayi:
        print("Aşağı")
        skor-=20
    else:
        print("Yukarı")  
        skor-=20  

print(f"Skorunuz: {skor}")
