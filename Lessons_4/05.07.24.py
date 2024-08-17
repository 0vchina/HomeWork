#Задание 1
i=1
while i<11:
    print(i)
    i+=1
# Задание 2
n=int(input('Введите число a='))
i=1
while i<n:
    print(i)
    i+=1
# Задание 3
i=0
while i<20:
    print(i)
    i+=2
# Задание 4
n=int(input('Введите число a='))
i=0
while i<n:
    print(i)
    i+=2
# Задание 5
i=1
while i<10:
    i2=1
    print()
    while i2 < 10:
        print(f'{i}*{i2}={i*i2}')
        i2+=1
    i+=1
# Задание 6
n=int(input('Введите число a='))
i=1
while i<n:
    i2=1
    print()
    while i2 < 10:
        print(f'{i}*{i2}={i*i2}')
        i2+=1
    i+=1
# Задание 7
n=int(input('Введите число a='))
while n>0:
    print(n)
    n-=1
# Задание 8
i=97
while i<122:
    print(chr(i), chr(i-32))
    i+=1
# Задание 9
n=input('Введите слово:')
l=len(n)-1
s="Слово наоборот:"
while l>=0:
    s=s+n[l]
    l-=1
print(s)
# Задание 10
n=input('Введите слово:')
l=0
s="Слово без буквы (а):"
while l<len(n):
    d=n[l]
    if d.lower()!='a' and d.lower()!='а':
        s=s+n[l]
    l+=1
print(s)
# Задание 11
n=input('Введите слово:')
g='euyioaуеыаоэяиюё'
l=len(n)
f=0
for i in n:
    if i in g:
        f+=1
print(f'Количество гласных в слове = {f} штук')
# Задание 12
n=input('Введите текст:')
n = n.split()
f=0
d=['a','A','а','А']
for i in n:
    for k in d:
        if k in i:
            f+=1
print(f'Количество слов с букыой а = {f} штук')
# Задание 13
n=input('Введите текст:')
n=n.lower()
i=97
spicok_bukf=''
result=''
while i<122:
    spicok_bukf=spicok_bukf+chr(i)
    i+=1

for e in n:
        if e in spicok_bukf:
        	result=result+' '+str(spicok_bukf.find(e))
print(result)