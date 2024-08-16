# задача 1
m=[[1,2,3,4], [2,3,4,5], [3,4,5,6], [4,5,6,7]]
def sum(mat, a):
    s=0
    for x in mat:
        s+=x[a]
    return s
print(sum(m,3))
# задача 2
s='22.12.2024'
# задача 2
def d(a):
    s=[int(x) for x in a.split('.')]
    return f'{s[2]}-{s[1]}-{s[0]}'
print(d(s))