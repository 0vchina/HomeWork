import book
from datetime import datetime
#словарь- в ключе номер книги, в значении ID пользователя
k = {2: 0, 3: 3}
#логфайл
log={}

#Функция выводит списо доступных книг и выдаёт книгу.
def inf1(dic, e):
    print(f'Список доступных книг:\n {dic}')
    print('Ведите номер книги или exit для выхода:')
    n = input()
    if n == 'exit':
        print('до свидания')
        log[datetime.now()] = f'Пользователь: {e[2]} вышел из системы'
        return 'exit'
    elif n.isdigit():
        if int(n) in book.lib2.keys():
            k[int(n)] = e[1][e[2]]
            dic = book.lib2.copy()
            for j in k.keys():
                del dic[j]
            log[datetime.now()] = f'Пользователь: {e[2]} взял книгу: {book.lib2[int(n)]} c номером: {int(n)}'
            print(f'Вы взяли книгу: {n}:{book.lib2[int(n)]}')
            print(f'Список доступных книг:\n {dic}')

            return 'exit'
        else:
            print('Книги с таким номером нет')
            return 'exit'
    else:
        print('Некорректно введены данные')
        return 'exit'

#Функция выводит список доступных книг и принимает книгу.
def inf2(dic, e):
    dd = {i: book.lib2[i] for i in k.keys() if k[i] == e[1][e[2]]}
    print(f'Список книг(взятые вами ранее):\n {dd}')

    if dd=={}:
        print('Вы не можете сдать книгу. Вы ее еще её не взяли.')
        print('Хотите ли вы взять книгу или выйти?(Y/N)')
        w = input()
        if w == 'y' or w == 'Y':
            return inf1(dic, e)
        elif w == 'n' or w == 'N':
            return 'exit'
        else:
            print('некорректно введены данные')
            return 'exit'
    print('Ведите номер книги или exit для выхода:')
    n = input()
    if n == 'exit':
        print('до свидания')
        log[datetime.now()] = f'Пользователь: {e[2]} вышел из системы'
        return 'exit'
    elif n.isdigit():
        if int(n) in book.lib2.keys():
            del k[int(n)]
            dic = book.lib2.copy()
            for ii in k.keys():
                del dic[ii]
            log[datetime.now()] = f'Пользователь: {e[2]} сдал книгу: {book.lib2[int(n)]} c номером: {int(n)}'
            print(f'Вы сдали книгу: {n}:{book.lib2[int(n)]}')
            print(f'Список доступных книг:\n {dic}')
        else:
            print('Книги с таким номером нет')
            return 'exit'
    else:
        print('Некорректно введены данные')
        return 'exit'



def inf(y, e):
    dic = book.lib2.copy()
    for i in k:
        del dic[i]
    ddd = {i:book.lib2[i] for i in k.keys()}
    print(f'Список книг на руках у пользователей:\n {ddd}')
    if y=='y' or y=='Y':
        return inf1(dic, e)


    elif y=='n' or y=='N':
        return inf2(dic, e)

    elif y == 'exit':
        return 'exit'

    else:
        print('Некорректно введены данные')
        return 'exit'


