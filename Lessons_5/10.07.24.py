#задание 1
a=int(input('Введите а='))
b=int(input('Введите b='))+1
c=[x**2 for x in range(a,b)]
print(c)
#задание 2
a=int(input('Введите а='))
b=int(input('Введите b='))+1
c=[x for x in range(a,b) if x%2==0]
print(c)
#задание 3
array=input('Введите строку:')
s='aeuioyаеыоэяиюй'
c=[x for x in array if x in s]
print(c)
#задание 4
c=[x for x in range(1,100) if x%3==0 and x%5==0]
print(c)
#задание 5
a=int(input('Введите а='))
c=[[x,x+1,x+2,x+3] for x in range(0,a)]
print(c)
#задание 6
ss=['vhsjebshsjs', 'hheuhe777738363gdu', '73838388327', '1']
c=[x for x in ss if x.isdigit()]
print(c)
#задание 7
a=input('введите число:')
c=[int(x) for x in a if a.isdigit()]
print(max(c))

#задание 8
s='is2 Thi1s T4est 3a'
f = s.split()
ss=[x for x in s if x.isdigit()] 
dick={x: f[ss.index(x)] for x in ss}
ss.sort()
[print(dick[t]) for  t  in ss]

#задание 9
l=[{'имя':'вова', 'возраст':10,  'оценки':'плохие'}, {'имя':'илья', 'возраст':30,  'оценки':'хорошие'}, {'имя':'иван', 'возраст':4,
  'оценки':'плохие'}]
l2=[y['возраст'] for y in [x for x in l]]
d2={l2[x]:l[x] for x in range(0, len(l))}
print(d2)
for i in range(len(l2)):
	for k in range(len(l2) - 1 - i):
		 	 if l2[k] > l2[k + 1]:
		 	 	 l2[k], l2[k + 1] = l2[k + 1], l2[k]
[print(d2[t]) for  t  in l2]
