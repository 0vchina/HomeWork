#1)Создание книг – книги имеют название, автора и код. У одного автора может быть несколько книг
lib = {0:["Уллис","Джеймса Джойса"],2:["Человек-невидимка","Ральфа Эллисона"],3:["На маяк","Вирджинии Вулф"],4:["«Божественная комедия","Данте Алигьери"],
       5:["«Путешествия Гулливера»","Джонатан Свифт"], 6:["Мидлмарч"," Джордж Элиот"]}
lib2=lib
def creat_book():
    x=0
    while x!="exit":
        print(f'Список книг в библиотеке:\n{lib2}')
        print('-введите название книги и автора этой книги\n -для выхода введите: exit')
        x=input()
        if x=="exit":
            return lib2
        y=input()
        ch = 0
        for ch in lib2.keys():
            ch += 1
        lib2[ch]=[x,y]
        ch+=1

    return lib2

