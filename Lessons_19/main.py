from random import randint
import multiprocessing
class team:
    def __init__(self, name):
        self.name=name
    def __repr__(self):
        return f'{self.name}'
    def __str__(self):
        return f'{self.name}'
    @property
    def nam(self, value):
        self.name=value

l=[
   ['1-то целое число?','да', 2],['2-то это отрицательное число?','нет', 1], ['10-это четное или нечетное число?', 'четное', 4],
   ['11-это это дробное число?','нет', 3], ['A-это первая буква?','да', 2], ['Я-это не первая цифра?','нет', 3],
   ['D-это русская буква?','нет', 2], ['1010-это 10 на двоичном?','да', 10], ['1011-это на двоичном?','11', 2],
   ['1-то целое число?','да', 2],['2-то это отрицательное число?','нет', 1], ['10-это четное или нечетное число?', 'четное', 4],
   ['11-это это дробное число?','нет', 3], ['A-это первая буква?','да', 2], ['Я-это не первая цифра?','нет', 3],
   ['D-это русская буква?','нет', 2], ['1010-это 10 на двоичном?','да', 10], ['1011-это на двоичном?','11', 2],
   ['1-то целое число?','да', 2],['2-то это отрицательное число?','нет', 1], ['10-это четное или нечетное число?', 'четное', 4],
   ['11-это это дробное число?','нет', 3], ['A-это первая буква?','да', 2], ['Я-это не первая цифра?','нет', 3],
   ['D-это русская буква?','нет', 2], ['1010-это 10 на двоичном?','да', 10], ['1011-это на двоичном?','11', 2]
   ]



def limited_time_function(func, timeout, *args, **kwargs):
    with multiprocessing.Pool() as pool:
        result = pool.apply_async(func, args, kwargs)
        try:
            return result.get(timeout=timeout)
        except multiprocessing.TimeoutError:
            print("Function timed out!")
            return None



class answers:
    def __init__(self, question, answ, team, answnum):
        self.question=question
        self.answ=answ
        self.team=team
        self.answnum=answnum

    def bal(self):
        if self.question[1]!=self.answ.lower():
            self.ball = 0
            return self.ball
        self.ball = self.question[2]
        return self.ball

    def result(self):
        return [self.team, self.bal(),self.answnum,self.question,self.answ]


    def __repr__(self):
        return (f'{self.answnum} вопрос для команды {self.team}: {self.question[0]} \n'
                f' ответ команды:{self.answ}\n правильный ответ:{self.question[1]}\n{self.bal()}')
    def __str__(self):
        return (f'{self.answnum} вопрос для команды {self.team}: {self.question[0]} \n'
                f' ответ команды:{self.answ}\n правильный ответ:{self.question[1]}\n{self.bal()}')


def check(i):
    while True:
        if i.isdigit():
            if int(i) > 0:
                return i
        print('неправильно:')
        i = input('ведите число команд:')
def check1(i):
    while True:
        if i.isdigit():
            if int(i) == 0 or int(i) == 1:
                return i
        print('неправильно:')
        i = input('ведите номер ответа:')
def check2(i):
    while True:
        if i!='':
            return i
        print('неправильно:')
        i = input('ведите название команды:')



def opros_team(i,j):
    l2 = l
    rr = {0: 'нет', 1: 'да'}
    h = l2[randint(0, len(l2) - 1)]
    print(h[0])
    if h[1] == "да" or h[1] == "нет":
        print('да-1')
        print('нет-0')
        r = int(check1(input()))
        ff=answers(h, rr[r], j, i)
        l2.remove(h)
        return ff
    else:
        print('введите ответ:')
        r = check1(input())
        ff=answers(h, r, j, i)
        l2.remove(h)
        return ff



def opros(ll):
    dd = []
    for j in ll:
        for i in range(1,3):
            print(f'{i} вопрос для команды: {j}')
#            f=limited_time_function(opros_team(i, j), timeout=10)
            f = opros_team(i, j)
            dd.append(f)
    return dd



def run():
    d = check(input('ведите число команд:'))
    ll = []
    for i in range(int(d)):
        ll.append(team(check2(input())))
    print(ll)
    print('Начинается опрос:')
    dd=opros(ll)

    print('Опрос окончен:')
    gg = {}
    for i in ll:
        print(f'Команда:{i}')
        b = 0
        for j in dd:
            y = j.result()
            if y[0] == i:
                print(f'{y[2]}:{y[3][0]}---->ответ:{y[4]}---->правильный ответ:{y[3][1]}---->получает:{y[1]}')
                b += int(y[1])
        gg[i] = b
    return print(gg)




run()
