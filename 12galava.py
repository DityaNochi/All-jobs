class Hexagon():

    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.perimetr1 = p1
        self.perimetr2 = p2
        self.perimetr3 = p3
        self.perimetr4 = p4
        self.perimetr5 = p5
        self.perimetr6 = p6

    def calculate_perimetr(self):
        return self.perimetr1 + self.perimetr2 + self.perimetr2 + self.perimetr3 + self.perimetr4 + self.perimetr5 + self.perimetr6

plosh = Hexagon(2, 3, 4, 5, 6, 7)
print(plosh.calculate_perimetr())




'''
class Triangle():
    def __init__(self, o, v):
        self.osnovanie = o
        self.visota = v

    def area(self):
        return self.osnovanie * self.visota / 2

tri = Triangle(10, 5)
print(tri.area())
'''


'''import math

class Circle:
    def __init__(self, r):
        self.radius = r
        print("Created")

    def area(self):
        return math.pi * self.radius ** 2

krug = Circle(10)
print(krug.area())
'''

'''class Apple:
    def __init__(self, c, m, k, t):

        self.color = c
        self.massa = m
        self.kolich = k
        self.tcena = t
        print("Created")

    def pokaz(self, kolichestvo, chena):
        self.pokaz = kolichestvo * chena

apple = Apple("red", 12, 1, 35)
print(apple.color)
print(apple.massa)
print(apple.kolich)
print(apple.tcena)

apple.pokaz(12, 33)
print(apple.pokaz)
'''
