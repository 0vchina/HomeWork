#задача1
products = ['apple', 'orange', 'milk']
count=[1,3,12]
def f(x,y):
    if len(x)!=len(y):
        return "списки разные по длине"
    else:
        return {i:y[x.index(i)] for i in x}
print(f(products,count))
#задача2
def ff(x):
    d=2
    for i in range(2,int(x)):
        if int(x)%d==0:
            return 'число не простое'
        else:
            d+=1
    return 'число простое'
x=input("Вводите числа для проверки на простое или не простое это число(для выхода введите: exit):")
def s(x):
    while x!='exit':
        print(ff(x))
        x = input()
    else:
        return 'программа окончена'
print(s(x))
#задача3
def q(i):
    ii=i[::-1]
    i1=i
    ii1 = i1[::-1]
    if i==ii:
        return f'число {i} уже палиндром'
    else:
        while i!=ii and i1!=ii1:
            i=str(int(i)+1)
            ii = str(i)[::-1]
            i1 = str(int(i1) - 1)
            ii1 = str(i1)[::-1]
        else:
            if i==ii:
                return f'ближайший полиндром: {i}'
            return f'ближайший полиндром: {i1}'
print(q(input("Введите число для поиска полиндрома: ")))
#задача4
def fff(x,y):
    mn = int(min(x,y))
    mx = int(max(x,y))
    mx1=mx+1
    if mx%mn==0:
        return f'наименьшнее кратное двух чисел:{mx}'

    else:
        while mx1%mn!=0 or mx1%mx!=0:
            mx1+=1
        else:
            return f'наименьшнее кратное двух чисел:{mx1}'
print(fff(int(input('введите первое число:')),int(input('введите второе число:'))))
#задача 5
import random
def r(x,y):
    len=random.randint(0, int(x))
    return [random.randint(0, int(y)) for i in range(0,len)]

def sum(x):
    s=list(set(x))
    d={xx:0 for xx in s}
    for i in x:
        d[i]=d[i]+1
    return d

print(sum(r(input('введите диапазон из которого будет выбираться длина списка:'),input('введите диапазон из которого будт выбираться числа для списка:'))))
