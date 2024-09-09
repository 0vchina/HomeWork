#Задача №2
class man:
    def __init__(self, name, age, h):
        self.name=name
        self.age=age
        self.h=h
    def get_name(self):
        return f'{self.name}'
    def new_name(self,value):
        self.name = value
    def del_name(self):
        self.name = None
    pr=property(fget=get_name, fset=new_name, fdel=del_name)

    def get_age(self):
        return f'{self.age}'
    def new_age(self,value):
        self.age = value
    def del_age(self):
        self.age = None
    pr=property(fget=get_age, fset=new_age, fdel=del_age)

    @property
    def ph(self):
        return f'{self.h}'
    @ph.setter
    def ph(self, value):
        self.h = value
    @ph.deleter
    def ph(self):
        self.h = None

#Задача №3
class circle:
    def __init__(self, r):
        self.r=r

    def square(self):
        return f'площадь:{3.14*self.r*self.r}'

    @property
    def check_r(self):
        return f'{self.h}'

    @check_r.setter
    def check_r(self, value):
        self.r = value

    @check_r.deleter
    def check_r(self):
        self.r = None

#Задача №4
class bank:
    def __init__(self, balance):
        self.balance=balance

    def iin(self, value):
        self.balance+=value
    def out(self, value):
        if self.balance<value:
            return print('недостаточно денег')
        self.balance-=value
    @property
    def check_balance(self):
        return f'{self.balance}'

    @check_balance.setter
    def check_balance(self, value):
        self.balance = value


#Задача №5
class phone:
    def __init__(self, name, color, price):
        self.name=name
        self.color=color
        self.price=price

    def sale(self):
        if self.price<50:
            return print(f'нет скидки')
        return print(f'скидка 10% = {self.price*0.1}$')


    @property
    def check_name(self):
        return f'{self.name}'

    @check_name.setter
    def check_name(self, value):
        self.name = value

    @property
    def check_color(self):
        return f'{self.color}'

    @check_name.setter
    def check_color(self, value):
        self.color = value

    @property
    def check_price(self):
        return f'{self.price}'

    @check_name.setter
    def check_price(self, value):
        self.price = value


class Warrior:
    def __init__(self):
        self._expirience=100
        self._level=1
        self.achievements=[]
    def rank(self):
        if self._level in range(1,10):
            return print('Pushover')
        elif self._level in range(10,20):
            return print('Novice')
        elif self._level in range(20,30):
            return print('Fighter')
        elif self._level in range(30,40):
            return print('Warrior')
        elif self._level in range(40,50):
            return print('Veteran')
        elif self._level in range(50,60):
            return print('Sage')
        elif self._level in range(60,70):
            return print('Elite')
        elif self._level in range(70,80):
            return print('Conqueror')
        elif self._level in range(80,90):
            return print('Champion')
        elif self._level in range(90,100):
            return print('Master')
        else:
            return print('Greatest')
    def edit_expirience(self,value):
        if self._expirience < 10000:
            self._expirience += value
        if self._expirience > 10000:
            self._expirience = 10000
            self._level = 100
        else:
            for i in range(1,100):
                if self._expirience < i*100:
                    self._level = i-1
            return 0

    def training(self, nam, exp, lev):
        if self._level >= lev:
            self.edit_expirience(exp)
            self.achievements.append(f'Defeated {nam}')
        else:
            print('Not strong enough')

    def fight(self, other):
        if self._level==other._level:
            self.edit_expirience(10)
            return "A good fight"
        elif self._level-other._level==1:
            self.edit_expirience(5)
            return "A good fight"
        elif self._level-other._level>=2:
            self.edit_expirience(0)
            return "Easy fight"
        elif other._level-self._level>=1 and other._level-self._level<=5:
            self.edit_expirience(20*(other._level-self._level)*(other._level-self._level))
            return "An intense fight"
        else:
            return "You've been defeated"

    @property
    def check_expirience(self):
        return f'{self._expirience}'

    @property
    def check_level(self):
        return f'{self._level}'


b_lee=Warrior()
f_lee=Warrior()
print(b_lee.check_expirience)
b_lee.training('djorsh', 2000, 1)
b_lee.training('djorsh', 10000, 21)
print(b_lee.check_expirience)
print(b_lee.achievements)
print(b_lee.check_level)
b_lee.rank()
