#Пока я это делал - я ебанулся. Пиздец, мне некуда выговорится, но я себя
#сейчас не умным чусвствую, а неуверенно. Ибо я думаю что местами схитрил
#либо функция выполнена не совсем верно, так например история с классом
#Shape - я придумал ебучюю __init__, хотя мог спокойно придумать принт - и всё!
#крч я разбился об самого себя, я обхвалился, так нельзя. В следующие разы я если
#и буду что-то показывать, то чтобы и Я и те кому показываю поучаствовали в этом
#И я не выебываюсь а просто пишу код и практикуюсь и им будет интересней смотреть как я горю
#И МОЖЕТ БЫТЬ ДАЖЕ ПОБЕЖДАЮ СВОЙ КОД:D
#Я считаю что перед сном сделал достаточно, мне осталось почитать пока не надоест и после сна
# закрепить то, что прочитал! :)

class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self,
                 rost,
                 ves,
                 vsadnik):
        self.rost = rost
        self.ves = ves
        self.vsadnik = vsadnik


loshad = Horse("Luna")
naezdnik = Rider("175", "73kg", loshad)

print(naezdnik.vsadnik.name)


"""
"""
class Shape():
        def what_am_i(self):
            print("""Am i a figure:)""")
"""

class Rectangle(Shape):

    def __init__(self, d, s):
        self.dlina = d
        self.shirina = s

    def calculate_perimeter(self):
        return (self.dlina + self.shirina) * 2




class Square(Shape):

    def __init__(self, d):
        self.dlina = d

    def calculate_perimeter(self):
        return self.dlina * 4

    def change_size(self, new_size):
        self.dlina += new_size

text_re = Rectangle(4, 2)
text_sq = Square(4)

text_re.what_am_i()
text_sq.what_am_i()

"""

"""

#a_rectangle = Rectangle(5, 4)
#print(a_rectangle.calculate_perimeter())
a_shape = Shape(2)
a_shape.what_am_i()

a_square = Square("Hto ya?")
a_square.what_am_i()
a_rectangle = Rectangle("Ne yasno")
a_rectangle.what_am_i()
#print(a_square.dlina)
#a_square.change_size(4)
#print(a_square.dlina)

"""

'''class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed  #poroda
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jugger")
stan = Dog("Stainly", "Bulldog", mick)
print(stan.owner.name)
'''

'''
class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} на {}
              """.format(self.width,
                         self.len))

my_shape = Shape(20, 30)
my_shape.print_size()


#Дочерний класс Square использует функционал класса Shape
class Square(Shape):
    def area(self):
        return self.width * self.len

def print_size(self):
    print("""{} на {}
          """.format(self.width,
                     self.len))


a_square = Square(25, 40)
a_square.print_size()
'''


#Это хрень, она ненужна
"""class Square():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def change_size(self):
        e = 2
        self.a += e
        self.b += e
        self.c += e

sq = Square(1, 2, 3)
print(sq.change_size())


"""
