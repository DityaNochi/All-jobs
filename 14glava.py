"""def sravnenie(a, b):
    return a is b


print(sravnenie(4, 6))
print(sravnenie("b", "b"))

"""


class Square():
    square_list = []

    def __init__(self, s):
        self.shape = s
        self.square_list.append(self)

    def __repr__(self):
        return """{} na {} na {} na {}""".format(self.shape,
                                                 self.shape,
                                                 self.shape,
                                                 self.shape)



s1 = Square(4)
s2 = Square(27)

print(s1, s2)
print(Square.square_list)





"""
x = 10
if x is None:
    print("x ravno None:(")
else:
    print("x Ne ravno None")

x = None
if x is None:
    print("x ravno None")
else:
    print("x ravno None :*")
"""

"""
#Ключевое слово IS
class Person():

    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print (bob is same_bob)

another_bob = Person()
print(bob is another_bob)
"""

"""
class AlwaysPossitive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs (self.n +
                    other.n)

x = AlwaysPossitive(-20)
y = AlwaysPossitive(14)

print(x + y)
"""

'''
#Магич. методы
class Lion():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Дилберт")
print(lion)

'''



'''
Переменные класс и переменные экземпляров класса
class Rectangle():
    recs = []

    def __init__(self, w, l ):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("""{} Na {}"""
              .format(self.width, self.len))


m_rectangle = Rectangle(10, 24)
r2 = Rectangle(150, 255)
m_rectangle.print_size()

print(Rectangle.recs)
'''
