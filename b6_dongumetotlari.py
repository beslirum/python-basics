#range(başlangıç_değeri, bitiş_değeri, artış_değeri)

# for item in range(50,100,10):
#     print(item)

# print(list(range(50,100,10))) #listeledik

###########

#enumerate
# Enumerate methodu iki parametre alır. 
# Birinci parametre itere edilecek objedir yani bir iterabledır.
#  Örneğin bir list, tuple, yada string gibi. 
#  İkinci parametre ise start parametresidir ve indexlenmenin kaçtan başlayacağını belirler. 
#  Bu parametre opsiyoneldir, istersek kullanmayabiliriz ama bu durumda index 0'dan başlayacaktır.

# greeting = 'Hello There'

# for item in enumerate(greeting):
#     print(item)
#     # print(f'letter: {greeting[index]} index: {index}')
#     # index+=1

###########

#zip
#zip() fonksiyonu, iki dizisel elemanın öğelerini birbirleriyle eşleştirirerek bir zip objesi oluşturur.
list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)

