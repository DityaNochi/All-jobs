lists = []
rap = ["atl",
       "ynnv",
       "rinok"]

post = ["Doma",
        "angliya",
        "shit"]
dj = ["pon3",]

lists.append(rap)
lists.append(post)
lists.append(dj)
print(lists)

dj = lists[0]
print(dj)

dj = lists[2]
dj.append("locked club")
print(dj)











"""fruits = {"яблоко":
          "красное",
          "банан":
          "желтый"}

print (fruits)


fruits["яблоко"] ="""








"""fruit = ["1", "2", "3"]
guess = input("Угадай цвет:")

if guess in fruit:
    print("Угадал")
else:
    print("Не угадал")"""



















"""    #code
def age (string):
    '''Документации?, я бля уже все задокументировал все то, что я делал, нихуя не понял, буду еще пытатся, но уже внятно
    воть'''
        try:
            return float(string)
        except ValueError:
            print("Цифры а не буквы, епта")
 
a = age("eee")

print(a)
"""


















"""
def odin(x):
    return x / 2

def dva(a):
    return a*4
result = odin(10)
z = dva(result)
print(z)
"""





















"""
def f(z,x,c, a=10, b=20,):
      return z + x + c * a * b

result = f(10, 2, 3, 4)
print(result)
"""





















"""try:
    a = int(input("число 1 :"))
    b = int(input("число 2 :"))

    print(a / b)
except (ZeroDivisionError, ValueError):
    print("1 и 2 не может быть нулем либо буквой") """
