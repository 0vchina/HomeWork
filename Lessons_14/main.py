import users
import info
import book

users1 = input('Введите фамилию и имя пользователя:')

def libruary(us1):
    while us1 != 'exit':
        if us1 == 'admin':
            r=input('-создать новую книгу(1), список пользователей(2) или посмотреть log файл?(3)')
            if r=='1':
                book.creat_book()
            elif r=='2':
                print(users.users2)
            elif r=='3':
                print(info.log)
            else:
                print('Выход или не корректно ввеены данные')
        else:
            ff = users.сheck_users(us1)
            if ff == False:
                print('Выполняется выход...')
                return 'exit'
            else:
                y = input('Вы ходите взять книгу(Y) или сдать книгу(N)?')
                info.inf(y, ff)
        us1 = input('Введите фамилию и имя пользователя:')

libruary(users1)