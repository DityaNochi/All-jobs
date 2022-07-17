def bigger(a,b):
    if a > b:
        return a # Если a больше чем b, то возвращаем a и прекращаем выполнение функции
    return b # Незачем использовать else. Если мы дошли до этой строки, то b, точно не меньше чем a

# присваиваем результат функции bigger переменной num
num = bigger(23,42)

print(num)











'''import statistics

a = [1, 5, 63, 361, 33, 44, 1, 7]

print(statistics.mean(a))
'''
'''import math
math.pow(2, 3)
'''
