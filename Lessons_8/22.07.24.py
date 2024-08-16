#задача 1
s=[1, 2, 3, 4, 5, 8, 65, 43, 4, 4444]
ss=list(filter(lambda x: x%2==0, s))
print(ss)
#задача 2
x=1
y=99
a= lambda x,y: x+y
print(a(x,y))
#задача 3
w=['dawdwad', 'dadd', 'd', 'scac', 's']
w1=list(filter(lambda x: len(x)>3, w))
print(w1)
#задача 4
s=[1, 2, 3, 4, 5, 8, 66, 43, 4, 4444]
s1=list(map(lambda x: x**2, s))
print(s1)
#задача 5
w=['dawdwad', 'Adadd', 'd', 'scac', 'as']
s=list(filter(lambda x: x.lower().startswith('a'), w))
print(s)
#задача 6
s=[1, 2, 3, 4, 5, 8, 65, 43, 4, 4444]
d=list(filter(lambda x: x>10, s))
print(d)
#задача 7
w=['dawdwad', 'Dadd', 'd', 'scac', 'S']
w2=list(filter(lambda x: x.isupper(), w))
print(w2)
#задача 8
s=[1, 2, 3, 4, 5, 8, 66, 43, 4, 4444]
q=list(filter(lambda x: x%3==0, s))
print(q)
#задача 9
s=[1, 2, 3, 4, 5, 8, 66, 43, 4, 4444]
q=list(filter(lambda x: x>=5 and x<=10, s))
print(q)
#задача 10
w=['dawdwad', 'Adaddjo', 'd', 'scac', 'as', 'o']
s=list(filter(lambda x: x.lower().endswith('o'), w))
print(s)
#----------------------------
#-----------------------------
#задача 1
w=['dawdwad', 'Adadd', 'd', 'scac', 'as', 'skhdgajhsgda']
l=[len(x) if len(x)>5 else x for x in w]
print(l)
#задача 2
dict1={x:x if x%2==0 else x**2  for x in range(1,10)}
print(dict1)
#задача 3
l=[1, 3, 5]
l2=[2]
l3=[1, 3, 5]
s1=[l+l2 if l!=l2 else 'списки равны']
s2=[l+l3 if l!=l3 else 'списки равны']
print(s1)
print(s2)
#задача 4
k=[x**3 if x%4!=0 else "FOUR" for x in range(1,100)]
print(k)
#задача 5
k1=["Fizz" if type(x) != str and x%3 == 0 else x for x in
    ["Buzz" if type(x) != str and x%5==0 else x for x in
     ["FizzBuzz" if x%15 == 0 else x for x in range(1,100)]]]
print(k1)
