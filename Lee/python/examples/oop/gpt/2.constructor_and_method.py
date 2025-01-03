import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    c0 = Circle(5)

    print(c0.area(),
    c0.circumference())