numbers = [1,2,3,4,5]

for num in numbers: #numberın eleman sayısı kadar döndürüyor
    print('Hello')

names = ["Rumeysa", "Ali", "Hamza", "Metehan", "aQif"]
for name in names:
    print(f'my crush list: {name}')

name = "Rumeysa Besli"

for n in name:
    print(n)

tuple = [(1,2), (1,3), (3,5)]
for a,b in tuple:
    print(a, b)

d = {'k1':1, 'k2':2, 'k3':3}
for item in d.items(): #d.items() ile eleman gruplarına ulaşılırken sadece in d deseydik '' içindeki bilgilere ulaşacaktık
    print(item)

for key, value in d.items():
    print(key, value)