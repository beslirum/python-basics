# global scobe

x = 'global x'

def function():
    x = 'local x'
    print(x)    #local x çıktısı
function()
print(x)    #global x çıktısı

#################
name = 'Rumeysa'
def changeName(new_name):
    name=new_name
    print(name)
changeName('Mete')
print(name)
#################
name = 'global string'
def greeting():
   # name='Rumeysa'

    def hello():
        #name='Ali'
        print('hello ' +name)

    hello()

greeting()

#########
x=50

def test():
    global x
    print(f'x: {x}')
    x=100
    print(f'changed x to {x}')

test()
print(x)

