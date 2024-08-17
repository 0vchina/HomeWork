
#задание№1
stroka = input('Введите строку:')
print (stroka.upper())
#задание№2
pod_stroka = input('Введите подстроку:')
if stroka.startswith(pod_stroka):
    print ("da")
else:
    print("net")
#задание№3
stroka=stroka.replace(pod_stroka,"!!!")
print (stroka)
#задание№4
print (stroka.split("!!!"))
#задание№5
print (stroka.strip())
#задание№6
a = ['efes', 'esfsef', 'efsfes', 'efsfes', 'sh', 'efsfes', 'efsfes', 'efsfes', 'efsfes']
b = ['sfef', 'csef']
a.extend(b)
print (a)
#задание№7
c=a.index("sh")
a.pop(c)
print (a)
#задание№8
s=[1, 2, 3, 5, 4, 6, 7]
s.sort()
print (s)
#задание№9
c=s.index(3)
print (c)
#задание№10
a = ['efes', 'esfsef', 'efsfes', 'efsfes', 'sh', 'efsfes', 'efsfes', 'efsfes', 'efsfes']
b = ['sfef', 'csef']
a.extend(b)
#задание№11
dict1= {"1":"one","2":"two", "3":"three", "5":"five"}
dict1["4"]={"four"}
print (dict1)
#задание№12
dict1.pop("4")
print (dict1)
#задание№13
if "2" in dict1:
    print('yes')
else:
    print('no')
#задание№14
print(dict1.keys())
#задание№15
print(dict1.values())
#задание№16
a = float(input("Введите число:"))
if a > 0:
    print(f"число {a}---Больше нуля")
elif a == 0:
    print(f"число {a}---Равно нулю")
else:
    print(f"число {a}---Меньше нуля")
#задание№17
a = float(input("Введите сторону а=:"))
b = float(input("Введите сторону b=:"))
c = float(input("Введите сторону c=:"))
if a == b and b==c:
    print("треугольник---равносторонний")
elif a == b or b==c or a==c:
    print("треугольник---равнобедренный")
else:
    print("треугольник---разносторонний")
#задание№18
a = input("Введите символ а=:")
if a == a.lower():
    print("нижний регистр букв или число")
else:
    print("верхний регистр букв или число")
#задание№19
a = input("Введите букву:")
list_glasnie= ["а", "е", "ё", "о", "у", "и", "э", "ы", "я", "ю"]
if a.lower() in list_glasnie:
    print(f"буква ({a})----- гласная")
else:
    print(f"буква ({a})----- согласная")
# задание№20
    a1 = int(input("Введите число а=:"))
    b1 = int(input("Введите число b=:"))
    c1 = int(input("Введите число c=:"))
if a1 == b1 and b1==c1:
    print('числа равны')
elif a1 > b1 and a1 > c1:
    print(f'число {a1} - больше')
elif b1 > a1 and b1 > c1:
    print(f'число {b1} - больше')
else:
    print(f'число {c1} - больше')
# задание№21
if len(stroka) > len(pod_stroka):
    print(f'строка (stroka) ---- больше по количеству символов')
elif len(stroka) < len(pod_stroka):
    print(f'строка (pod_stroka) ---- больше по количеству символов')
else:
    print('строки равны по количеству символов')
# задание№22
a = input("Введите номер месяца рождения:")
b ={"1":"январь-падал снег","2":"февраль-падал быстро снег","3":"март-немного начал таять снег","4":"арель-расстаял снег",
    "5":"май-почти лето","6":"июнь-лето", "7":"июль-жара", "8":"август-скоро осень", "9":"сентябрь-начало осени",
    "10":"октябрь-осень","11":"ноябрь-холодно", "12":"декабрь-дубак"}
if a in b:
    print(b[str(a)])
else:
    print('нет такого месяца')
# задание№23
a = input("Введите двухзначное число а=:")

if len(a) == len(set(a)):
    print("число состоит из разных цифр")
else:
    print("число состоит из одинаковых цифр")
# задание№24
a2 = input("Введите что-нибудь а=:")
if len(a2) ==0:
    print('false')
else:
    print('true')
# задание№25
a3 = input("Введите целое число а=:")
a4=str('kk')
a5=str('kkk')
a4=a4.replace('k', a3)
a5=a5.replace('k', a3)
print("n+nn+nnn=",(int(a3)+int(a4)+int(a5)))
# задание№26
dict1= {"one":1,"two":2, "three":3, "five":5}
print ("имеем словарь:",dict1)
dict1[(4,5,"yhh")]=[1, 2, 4, 'ghjj']
print ("Вставляем в словарь и получаем:",dict1)
print ("(two) из словаря:",dict1["two"])
del dict1[(4,5,"yhh")]
print ("имеем словарь после удаления:",dict1)
# задание№27
dictionary_1 ={'a':300, 'b':400}
dictionary_2 ={'c':500, 'd':600}
dictionary_1.update(dictionary_2)
print('Получаем словарь',dictionary_1)










