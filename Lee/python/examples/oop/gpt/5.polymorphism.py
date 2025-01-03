import math

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__()
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return (self.width * self.height)

class Circle(Shape):
    def __init__(self, range: float):
        super().__init__()
        self.range = float(range)

    def area(self):
        return (math.pi * (self.range ** 2))

if __name__ == "__main__":
    r0 = Rectangle(5, 10)
    c0 = Circle(5)
    print(f"r0's area: {r0.area()}, c0's area: {c0.area()}")