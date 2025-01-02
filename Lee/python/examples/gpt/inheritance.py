class Animal(object):
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def fetch(self):
        print(f"Dog named {self.name} is running to fetch the ball with make {self.sound} sound.")
        
if __name__ == "__main__":
    dodo = Dog("dodo", "walwal")
    dodo.fetch()