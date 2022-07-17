numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Угадай или х для выхода.")
    if answer == "x":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("vvedite chislo a ne bukvi, x dlya ostanovki")
    if answer in numbers:
        print("Verno")
    else:
        print("Neverno, x ili dalshe:")


'''
qs = ["Вопрос1?:",
      "Вопрос2?:",
      "Вопрос3?:"]

n = 0

while True:
    print("Введите х для остановки")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) % 3

print(8% 3)
'''


'''a = [8, 19, 148, 4]
b = [9, 1, 33, 83]
c = []

for i in a:
    for j in b:
        c.append(i * j)
print(c)
'''



'''a = ["Гав", "пиченьки", "лампа", "фембой", "Даллер Ковалевский"]

for i, b in enumerate(a):
    print(i)
    print(b)
'''



'''
for kall in a:
    slova = a[i]
    slova = slova.upper()
    a[i] = slova
    i += 1
print(a)
'''


'''for i in range(25, 51):
    print(i)
'''



'''
a = ["Гав", "пиченьки", "лампа", "фембой", "Даллер Ковалевский"]


for i in a:
    print(i)
'''










'''while input('a or b?') != "b":
    for i in range(1, 6):
        print(i)

'''





'''list1 = [1, 2, 3, 4, 5, 6]
list2 = [11, 12, 13, 14, 15, 16]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

'''










'''qs = ["Вопрос1?:",
      "Вопрос2?:",
      "Вопрос3?:"]

n = 0

while True:
    print("Введите х для остановки")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) % 3

print(8% 3)

'''








'''x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Отчет закончен!")
'''








'''tv = ["Unnv",
         "Neznakomci",
         "Ybiyci"]


for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new


print(tv)
'''
