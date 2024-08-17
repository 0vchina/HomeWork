def compas(comp):
    x, y = 0, 0
    for value in comp:
        if value.lower() == 's':
            y -= 1
        elif value.lower() == 'w':
            x -= 1
        elif value.lower() == 'e':
            x += 1
        elif value.lower() == 'n':
            y += 1
    return tuple([x,y])
i = input("Введите букву S,W,E,N: ")

def control_error(user):
    s=['s','w','e','n']
    if user == '':
        print("Вы ничего не ввели!")
        return 'swen'
    else:
        for x in user:
            if x.lower() not in s:
                print("Числа нельзя и любые другие символы нельзя")
                return 'swen'
        else:
            return user
        

def print_go(c: str):
    e=c.count('e')
    w=c.count('w')
    n=c.count('n')
    s=c.count('s')
    if abs(e-w)>100 or abs(n-s)>100:
        print("Вышли из зоны >100")
        return 'swen'
    else:
        return c    
print(compas(control_error(print_go(i))))