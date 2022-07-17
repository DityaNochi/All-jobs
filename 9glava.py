'''import csv
list = [["Звездные войный", "Терминатор", "Какой-то интелект"],
        ["Дурак", "Матильда", "Я - робот. долбаеб", "Деградация"]]
with open("nomerdva.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for movlist in list:
        w.writerow(movlist)
        '''
    """w.writerow(["Звездные войный", "Терминатор", "Какой-то интелект"])
    w.writerow(["Дурак", "Матильда", "Я - робот. долбаеб", "Деградация"])
    """
'''
#2
with open("dva.txt", "w") as f:
        f.write(input("Какой цвет я загадал?:"))
        print("Я подумаю над твоим ответом")
'''



'''
#1
with open("proverochka.txt", "r") as f:
    print(f.read())
'''



'''import csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter = ",")
    for row in r:
        print(" ".join(row))
'''


'''import csv

with open("st.csv", "w") as f:
    w = csv.writer(f,
                    delimiter=",")
    w.writerow(["Один",
                "Два",
                "Три"])
    w.writerow(["Новая строка началась!Четыре",
                "Пять",
                "Шесть"])
'''


'''listik = list()

with open("st.txt", "r") as f:
    listik.append(f.read())
print(listik)
'''



'''with open("proverochka.txt", "r") as f:
    print(f.read())
'''








'''
with open("proverochka.txt", "w") as f:
    f.write("Hi, mr Pidor")
'''


'''st = open("st.txt", "w")
st.write("Hello from python:)")
st.close
'''



"""import os
os.path.join("e:",
             "py new",
             "selfmadeprogrammer",
             "example.txt")
"""
