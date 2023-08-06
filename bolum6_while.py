#1-100 e kadar
'''
x = 0

while x <= 100:
    if x%2==0:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1

print('bitti...') '''

name = '' #False
while not name.strip(): #not name= true 
    name=input('isminizi giriniz: ')

print(f'Merhaba, {name}')


