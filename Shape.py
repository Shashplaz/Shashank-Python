import math


class Shape:
    def __init__(self, color, area):
        self.color = color
        self.area = area

    def area(self):
        print(self.area)

    def color(self):
        print(self.color)


class Square(Shape):
    pass

    def area(self, width, breath):
        area = width * breath
        print(area)


class Circle(Shape):
    from math import pi

    pass

    def area(self, radius):
        area = radius * math.pi
        print(area)
