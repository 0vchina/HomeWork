import book
from datetime import datetime
#словарь- в ключе номер книги, в значении ID пользователя
k = {2: 0, 3: 2}
#логфайл
log={}

def inf(y, e):
    dic = book.lib2.copy()
    for i in k:
        del dic[i]
    ddd = {i:book.lib2[i] for i in k.keys()}
    print(f'Список книг на руках у пользователей:\n {ddd}')
    if y=='y' or y=='Y':
        print(f'Список доступных книг:\n {dic}')
        print('Ведите номер книги или exit для выхода:')
        n=input()
        if n=='exit':
            print('до свидания')
            log[datetime.now()] = f'Пользователь: {e[2]} вышел из системы'
            return 'exit'
        else:
            if int(n) in book.lib2.keys():
                k[int(n)] = e[1][e[2]]
                dic = book.lib2.copy()
                for j in k.keys():
                    del dic[j]
                log[datetime.now()] = f'Пользователь: {e[2]} взял книгу: {book.lib2[int(n)]} c номером: {int(n)}'
                print(f'Список доступных книг:\n {dic}')
                return 'exit'

            else:
                print('Книги с таким номером нет')
                return 'exit'
    elif y=='n' or y=='N':
        print(e[1][e[2]])
        dd={i : book.lib2[i] for i in k.keys() if k[i]==e[1][e[2]]}
        print(f'Список книг(взятые вами ранее):\n {dd}')
        print('Ведите номер книги или exit для выхода:')
        n = input()
        if n == 'exit':
            print('до свидания')
            log[datetime.now()] = f'Пользователь: {e[2]} вышел из системы'
            return 'exit'
        else:
            if int(n) in book.lib2.keys():
                del k[int(n)]
                dic = book.lib2.copy()
                for ii in k.keys():
                    del dic[ii]
                log[datetime.now()] = f'Пользователь: {e[2]} сдал книгу: {book.lib2[int(n)]} c номером: {int(n)}'
                print(f'Список доступных книг:\n {dic}')
            else:
                print('Книги с таким номером нет')
                return 'exit'
    elif y == 'exit':
        return 'exit'
    else:
        print('Некорректно введены данные')
        return 'exit'


