# задание №1
a = input("Последовательность чисел (a):")
a = list(map(int, a.split(',')))
print (f'лист:{a}, кортеж:{tuple(a)}')
# задание №2
a = int(input("введите целое число а=:"))
if (a % 2) == 0:
   print (f'число a={a}-четное')
else:
   print (f'число a={a}-нечетное')
# задание №3
a = input("Введите строку через пробел  a=:")
a = list(map(int, a.split()))
b = {max(a), min(a)}
print(f'максимальное и минимальное значение={b}')
# задание №4
a = input("Введите целое число  a=:")
print('максимальная цифра в этом числе', max(a))
# задание №5
a = input("Введите имена пролайковших людей через заятую :")
a = list(map(str, a.split(',')))
b = len(a)
c = ['']
if a == c:
     print ('нет лайков:(')
elif b == 1:
     print (f'только один лайк от {a[0]} :(')
elif b == 2:
    print (f'двум людям понралилась запись: {a[0]} и {a[1]}')
elif b == 3:
     print (f'трём людям понралилась запись: {a[0]}, {a[1]} и {a[2]}')
else:
    print(f'поставил лайк: {a[-1]} и ещё {b-1}')
# задание №6
a = input("Введите слово:")
b = int(len(a))
c = int(len(set(a)))
if b > c:
   print(f'данное слово ({a}) является изограммой')
else:
   print(f'данное слово ({a}) НЕявляется изограммой')
# задание №7
a = int(input("Введите год:"))
b = a % 4
if b == 0:
    print(f'данный год ({a}) является високосным')
else:
    print(f'данный год ({a}) НЕявляется високосным')
# задание №8
a = float(input("Введите первую сторону треугольника:"))
b = float(input("Введите вторую сторону треугольника:"))
c = float(input("Введите третью сторону треугольника:"))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('возможно построить треугольник')
else:
    print('НЕвозможно построить треугольник')








