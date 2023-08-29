class Person:
    #class attributes
    address= 'no information'

    #constructor(yapıcı metod)
    def __init__(self, name, year):
        #object attributes
        self.name=name
        self.year=year
        print('init metodu çalıştırıldı')

    #instance methods
    def intro(self):
        print("Hello There. I'm " +self.name)

    def calculateAge(self):
        return 2023-self.year


#object
p1 = Person('Ahmet', 1998)
p2 = Person('mehmet', 2000)

p1.intro()
print(f"yasim: {p1.calculateAge()}")
p2.intro()
print(f"yasim: {p2.calculateAge()}")

############


class Circle:
    #class object attribute
    p=3.14
    def __init__(self, yaricap=1):
        self.yaricap=yaricap
    
    #methods
    def cevreHesapla(self):
        return 2 * self.p * self.yaricap
    def alanHesapla(self):
        return self.p * (self.yaricap**2)
    
c1 = Circle()       # yaricap = 1
c2 = Circle(5)

print(f'c1 : alan = {c1.alanHesapla()} . Cevre = {c1.cevreHesapla()}')
print(f'c2 : alan = {c2.alanHesapla()} . Cevre = {c2.cevreHesapla()}')