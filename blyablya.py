'''a = "И зачем так орать! Я и в первый раз, блаабалабаалб."
a = a[:17]
print(a)
'''

a = "три" #+ "три" + "три" метод конкатенации
a *= 3 #метод умножения
print(a)


'''p = "'Пятачок,' сказал Винни-Пух, 'по-моему, пчёлы что-то подозревают!'"
print(p)
'''














'''a = "Хемингуэй"


print(a.index("м"))
'''
'''stroka = "Ребенок - зеркало поступков родителей."

stroka = stroka.replace("о", "0")

print(stroka)
'''







'''aa = ["Рыжая", "лиса", "препрыгнула", "через", "низкий", "забор", "."]

result = " ".join(aa)

#Можно так(варик автора):
#result = result[0:-2] + "."
#А можно так(мой вариант):
result = result.replace(" .", ".")

print(result)
'''



'''print("Кто это?, Кто это?, Когда это?".split(","))
'''


'''
print("олдос Хаксли родился в 1894 году".capitalize())
'''



'''a = input("Введите строку 1: ")
b = input("Введите строку 2: ")

print("Вчера я написал {}." " Вчера я ходил в {}!".format(a,b))
'''





'''tab = [ "хуй",
        "давалка",
        "пенис",
        "хер",
        "давалка"]

print(tab[1:3])
'''


"хуй" in "хуй в жопе"
'''
"Залупа".index("п")
'''









'''a = "zamena na kall"

a = a.replace("a", "@")

print(a)
'''












'''a = ["hui",
     "penis",
     "davalka",
     "ssiklo"]

result = " ".join(a)

print(result.split(" "))
'''


































'''pi1 = input("Введите сущест.:")
glag = input("Введите глагол.:")
prilag = input("Введите прилаг.:")

c = 'ya ebal tvoy rot {}{}{}'.format(pi1,glag, prilag)



print(c.split(glag))'''




















#pi1 = input("Введите сущест.:")
#glag = input("Введите глагол.:")
#prilag = input("Введите прилаг.:")
#tab = '''Как всегда, {} {} {}
 #     '''.format(pi1,
  #               glag,
   #              prilag)
#print(tab)


























''''
actors = {'УННВ': 'Яма',
          'Англия': 'Ад из красных цветов',
          'Панкмодернисты': 'Чб',}

gruppa = input("Введите группу:")
if gruppa in actors:
    vivod = actors[gruppa]
    print(vivod)
else:
    print("Такой группы нет")
'''''




















''''pavel = ['УННВ', 'Англия', 'Агент', (51.65782112405248,39.14551873215536), (51.65341006926861,39.14876567077154) ]

profile = { 'дом':
            '51.65782112405248,39.14551873215536',
            'лента':
            '51.65341006926861,39.14876567077154',
            'Рост':
            '175см',
            'музыка':
            'Пост панк, УННВ (это не рэп, епты',
            'жизнь':
            'научится пользоватся Линуксом и создавать локальные сети, но ему лень('}



zapros = input('Введите запрос:')
if zapros in profile:
    result = profile[zapros]
    print(result)'''
