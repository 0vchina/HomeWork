class snow:
    sn=10

    def __add__(self, n1):
        return f'{'*' * (self.sn + n1)}'
    def __sub__(self, n1):
        return f'{'*' * (self.sn - n1)}'
    def __mul__(self, n1):
        return f'{'*' * (self.sn * n1)}'
    def __truediv__(self, n1):
        return f'{'*' * (self.sn / n1)}'

    def make_snow(self, n, nvr):
        for i in range(0,n//nvr):
            print(f'{'*'*nvr}')
        return (f'{'*' * (n%nvr)}')

f = snow()
print(f*5)
print(f.make_snow(31, 10))
