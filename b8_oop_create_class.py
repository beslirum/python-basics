#class
class Person:
    #class attributes
    address='no information'
    #constructor(yapıcı metod)
    def __init__(self, name, year):
    #self yerine this de denilebilir
    #object attributes
        self.name=name
        self.birthYear = year
        print('init metodu calisti')

    #methods

#object(instance)
p1 = Person(name='ali', year= 1999)
p2 = Person('Yagmur', 2002)

#updating
p1.name='Ahmet'

#accessing object attributes
print(f"name: {p1.name} year: {p1.birthYear} address: {p1.address}")
print(f"name: {p2.name} year: {p2.birthYear} address: {p2.address}")

print(p1)
print(p2)

print(type(p1))
print(type(p2))
print(p1 == p2)     #False çıktısı

