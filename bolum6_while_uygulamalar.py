sayilar = [1,3,5,7,9,12,19,21]
#sayilari while ile ekrana yazdir
'''
i=0
while ( i < len(sayilar)):
    print(sayilar[i])
    i+=1
'''
#başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
'''
baslangic = int(input("Baslangic degeri giriniz: "))
bitis = int(input("Bitis degeri giriniz: "))

i=baslangic
while i<bitis:
    i+=1
    if(i%2==1):
        print(i)
'''
#1-100 arasındaki sayıları azalan şekilde yazdırın
'''
index = 100
while index>=1:
    print(index)
    index-=1
'''
#kullanıcıdan alacağınız 5 sayıyı ekrana sayılı şekilde yazdır
'''
numbers = []
i=0
while i<5:
    sayi=int(input("sayı: "))
    numbers.append(sayi)
    i+=1
numbers.sort()      #sıraladık
print(numbers)
'''

#kullanıcıdan alacağınız sınırsız ürün bilgisini urunler list sakla
    #ürün sayısını kullanıcıya sor
    #dictionary lsit yapısı (name, price) şeklinde olsun
    #ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listele
urunler = []

adet=int(input("Ürün sayısını giriniz: "))
i=0
while i<adet:
    name= input("ürün ismi: ")
    price=int(input("ürün fiyatı: "))
    urunler.append({
        'name': name, 
        'price': price
    })
    i+=1
for urun in urunler:
    print(f'ürün adı : {urun["name"]} ürün fiyati : {urun["price"]}') #DIŞARIDA TEK TIRNAK İÇERİDE ÇİFT TIRNAK!!!!!!!!