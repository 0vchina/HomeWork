#2)Учет читателей – читатель имеет id, Фамилию и Имя. Один читатель может быть зарегистрирован в библиотеке один раз. Читатель может взять одновременно несколько книг

users2 = {'Овчинников Виталий':0,"Курчев Алексей":1,"Вечерко Юрий":3, "Макаревич Сергей":10, "Кирилкович Денис":14, "Макаревич Иван":11}
def сheck_users(x):
    if x in users2.keys():
        return [True, users2, x]
    else:
        y=input('хотите ли вы зарегистрироваться?(Y/N):')
        if y=='Y' or y=='y':
            z = input('Введите фамилию и имя нового пользователя:')
            k=z
            if len(z.split())!=2:
                print('не корректно введены данные')
                return False
            ch=0
            while ch in users2.values():
                ch += 1
            users2[f'{k.split()[0].capitalize()} {k.split()[1].capitalize()}']=ch
            print(f'Все пользователи(справочно):Admin,{users2}')
            return [True, users2, f'{k.split()[0].capitalize()} {k.split()[1].capitalize()}']
        else:
            print('некорректно введены данные')
            return False


