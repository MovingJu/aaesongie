class coffee:
    bean = str()
    
    def drip():
        print('coffee is being made.')

espresso = coffee()
americano = coffee()
espresso.bean = 'ethiopian'
americano.bean = 'american'
print(espresso.bean)
print(americano.bean)