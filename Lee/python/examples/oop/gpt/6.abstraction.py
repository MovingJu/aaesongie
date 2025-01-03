from abc import ABC, abstractmethod

class Venhicle(object):
    @abstractmethod
    def move(self):
        pass

class Car(Venhicle):
    def move(self):
        print("The car is driving.")

class Bicycle(Venhicle):
    def move(self):
        print("The bicycle is pedaling")

if __name__ == "__main__":
    c0 = Car()
    b0 = Bicycle()
    c0.move()
    b0.move()