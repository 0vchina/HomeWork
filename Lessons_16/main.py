import random

all_car=['bmw','opel','volkswagen','peugeot','renault','toyota','skoda','volvo']
all_country=['belarus','Russia' 'ukraine', 'polish', 'usa', 'britain']


class car:
    n=0
    def __init__(self, name, year, country):
        self.name = name
        self.year = year
        self.country = country
        car.n+=1
    def __eq__(self, other):
        return isinstance(other, car) and self.country == other.country

    def nul(self):
        self.year = 0
    def kol(self):
        return car.n

    def __str__(self):
        return f'{self.name} {self.year} {self.country}'
    def __repr__(self):
        return f'{self.name} {self.year} {self.country}'

def exemp(n):
    g=[]
    for i in range(0, n):
        g.append(car(random.choice(all_car), random.randint(1990, 2024), random.choice(all_country)))
    return g
h=exemp(10)
print(h)
print(h[9].kol())






