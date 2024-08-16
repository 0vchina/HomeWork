#задание 1
a=[32, 1, 4 , 5 , -6, 67, 23, 14, 64, 43, 17]
def kv(a):
	return [x**2 for x in a]
print(kv(a))
#задание 2
s=['fgsy', 'uhheg', ';^#&']
def ss(s):
	return [x for x in s if len(x)>=5]
print(ss(s))
#задание 3
def ch(a):
	return [x for x in a if x%2==0]
print(ch(a))
#задание 4
def skv(a):
	s=0
	for x in kv(ch(a)):
		s=s+x
	return (s)
print(skv(a))
#задание 5
k=['atyehsgys', 'hejdjdbdh', 'hjdhdhd', 'ahdhs', '1235']
def without_a(a):
	return [x for x in a if x[0]=='a']
print(without_a(k))
#задание 6
def t(a):
	return [x for x in a if x>10 and x<20]
print(t(a))
#задание 7
def ss_e(k):
	s=[]
	for x in k:
		for l in x:
			if l=='e':
				s.append(x)
	return s					
print (ss_e(k))
#задание 8
def xx(s):
	for x in s:
		if x<0:
			return False
	return True
print(xx(a))
#задание 9
def ww(a):
	return [x for x in a if x.isdigit()]
print(ww(k))
#задание 10
def e10(m):
	sss=[]
	for x in m:
		s=int(x)
		if x%2==0:
			while s>1:
				s=s/2
			if s == 1 and x!=1:
					sss.append(x)
	return sss				
print(e10(a))			
#задание доп. 1
def sa(a):
	s=0
	for x in a:
		s=s+int(x)**2
	return(s)
y=str(input('введите число='))
print(sa(y))
#задание доп.2
a=[1,5,2,7,4,9,6,6,7,4]
def sor(a):
	s=len(a)
	for z in range(s-1):
		for x in range(s-1-z):
			if a[x]%2==0 and a[x+1]%2!=0:
				a[x], a[x+1]=a[x+1], a[x]
	return a
print(sor(a))
#задание доп.3
def operation(start,end,step,operator):
	l=[x for x in range(start, end, step)]
	s=1
	ss=0
	match operator:
		case "+":
			for x in l:
				ss=ss+x
			return print('сумма ровна:',ss)
		case '-':
			for x in l:
				ss=ss-x
			return print('разница ровна:',ss)
		case '*':
			for x in l:
				s=s*x
			return print('произведение ровнo:',s)
		case '/':
			for x in l:
				s=s/x
			return print('деленик ровно:',s)
			
a=int(input('введите start='))
b=int(input('введите end='))
c=int(input('введите step='))
d=str(input('введите operator='))
print(operation(a,b,c,d))

#задание доп.4
aa=[32, 1, 4 , 5 , -6, 67, 23, 14, 64, 43, 17]
kk=['atyehsgys', 'hejdjdbdh', 'hjdhdhd', 'ahdhs', '1235']
def sd(x,y):
	return x+y
print (sd(aa,kk))