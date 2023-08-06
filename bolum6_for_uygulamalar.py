sayilar = [1,3,5,7,9,12,19,21]

#sayilar list. hangileri 3'ün katıdır?
print("3'ün Katları: ")
for kat in sayilar:
    if kat%3==0:
        print(kat)

#sayilar list. toplamı
print("Listedeki sayilarin Toplamı: ")
total=0
for tot in sayilar:
    total+=tot
print(total)

#sayilar list. tek sayıların karesi
print("Tek Sayıların Karesi: ")
for tek in sayilar:
    if tek%2!=0:
        print(tek*tek)


sehirler = ['Kocaeli', 'İstanbul', 'Ankara', 'İzmir', 'Rize', 'Malatya']
#şehirler dizisindeki hangileri max 5 karakterli
for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)

urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]
#urunlerin fiyatlar toplami nedir
toplam=0
print("Urunler toplami: ")
for urun in urunler:
    toplam+=int(urun['price'])
print(toplam)

#urunlerde fiyati max 5000 olani göster
for urun in urunler:
    if (int(urun['price'])) <= 5000:
        print(urun['name'])
