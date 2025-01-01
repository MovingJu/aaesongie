class JSS:
    def __init__(self):
        self.name = input('name: ')
        self.age = input('age: ')

    def show(self):
        print(f'{self.name}\'s age is {self.age}')


class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.gender = input("gender: ")

    def show(self):
        print(f'{self.name}\'s age is {self.age}, gender is {self.gender}')



a = JSS2()
a.show()
print(a.gender)