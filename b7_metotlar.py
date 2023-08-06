#method
list = [1,2,3]

list.append(4)
list.pop()      #son elemanı silen bir metod

print(type(list))
print(list)

myString= 'Hello'
print(myString.upper())
print(type(myString))

#fonksiyon
#def => define
def sayHello(name= 'user'):
    print('Hello '+name)

sayHello("Rumeysa")
sayHello("Yağmur")
sayHello()

def deneme(name='user'):
    return 'Hello ' +name
msg=deneme('Rumeysa')

print(msg)

def total(num1, num2):
    return num1+num2

result= (total(10,20))
print(result)

def yasHesapla(dogumYili):
    return 2023-dogumYili
ageRumeysa = yasHesapla(2002)
print(ageRumeysa)

def emekliligeKacYilKaldi(dogumyili, isim):
    '''
    DOCSTRING : Doğum yiliniza göre emekliliğinize kaç yil kaldi
    INPUT: Dogum Yili
    OUTPUT: Hespalanan yil bilgisi
    '''

    yas=yasHesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik>=0:
        print(f'{isim} Hanım, Emekliliğinize {emeklilik} yil kaldi')
    else:
        print(f'{isim} Hanım, Emeklisiniz.')
         
emekliligeKacYilKaldi(2002, 'Rümeysa')
emekliligeKacYilKaldi(1950, 'Yağmur')

print(help(emekliligeKacYilKaldi))

# list = [1,2,3]
# print(help(list.append()))



####################################################


def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'Çınar', age=2, city= 'İstanbul')
displayUser(name = 'Ada', age=12, city= 'Kocaeli', phone = '123456')
displayUser(name= 'yiğit', age=14, city= 'ankara', phone = '456789')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1='value 1', key2='value 2')
