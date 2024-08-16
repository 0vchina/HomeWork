import random
def x():
    pas =''
    a = [x for x in range(48, 57)]
    b = [x for x in range(65, 90)]
    c = [x for x in range(97, 122)]
    len = random.randint(8, 15)
    s = a + b + c
    for x in range(0, len):
        a=random.choice(s)
        pas+=str(chr(a))
    return pas
print(x())
print(x())
print(x())
#задача 4
def cpn(s):
    d='({}){}'.format(s[0:3],s[3:10])
    return d
f='1234567890'
print(cpn(f))
#задача 2
def game(p1, p2, p3):
    s={'камень':1, 'ножницы':2, 'бумага':3}
    if s[p1]!=s[p2] and s[p2]!=s[p3] and s[p1]!=s[p3]:
        return 'ничья'
    else:
        if s[p1] > s[p2] and s[p1]-s[p2]==1:
            if s[p1]>s[p3] and s[p1]-s[p3]==1:
                return 'первый игрок проиграл'
            elif s[p1]==s[p3]:
                return 'второй игрок проиграл'
            elif s[p1] < s[p3] and s[p3] - s[p1] == 1:
                return 'третий игрок проиграл'
            else:
                return 'третий игрок выйграл'
        elif s[p1] == s[p2]:
            if s[p1]>s[p3] and s[p1]-s[p3]==1:
                return 'третий игрок выйграл'
            elif s[p1]==s[p3]:
                return 'ничья'
            elif s[p1] < s[p3] and s[p3] - s[p1] == 1:
                return 'третий игрок выйграл'
            else:
                return 'третий игрок проиграл'
        else:
            if s[p2] > s[p3] and s[p2] - s[p3] == 1:
                return 'второй игрок проиграл'
            elif s[p2] == s[p3]:
                return 'первый игрок выйграл'
            elif s[p2] < s[p3] and s[p3] - s[p2] == 1:
                return 'третий игрок выйграл'
            else:
                return 'второй игрок выйграл'
print(game('ножницы', 'ножницы', 'камень'))