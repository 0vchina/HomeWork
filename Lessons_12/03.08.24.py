import time
from datetime import datetime
#задача1
def wait(x):
	def func(*args, **kwargs):
		time.sleep(0)
		return x(*args,*kwargs)
	return func
	 
@wait
def x(y):
		return 100*y
print(x(input()))
#задача 2
def log(x):
		def wap(*args, **kwargs):
			print('время начала операции:',datetime.now())
			print(x)
			print('время окончания операции:',datetime.now())
			print('результат:')
			return x(*args,**kwargs)
		return wap

@log
def x(y):
		return 100*y
print(x(input()))

#задача 3
def users(x):
	def wap(*args, **kwargs):
		user_type=input('введите тип пользователя:')
		if user_type=='admin':
			 	print('access')
			 	return x(*args, **kwargs)
		elif user_type=='user' or user_type=='auth_user':
			 	print ('denied')
			 	return 'выполнянтся выход'
		else:
			 	return 'denied---не корректно введены данные'
	return wap	

@users
def ent():
		return 'выполняется вход'		
print(ent())					
						
#задача 4
def annot(x):
	def wap(*args,**kwargs):
		dict1=x.__annotations__				
		dict2={**{x:type(x) for x in args},**{x:type(kwargs[x]) for x in kwargs}}
		dict2['return']=dict1['return']
		print (dict1)
		print(dict2)
		for i in dict1:
				for j in dict2:
					if dict1[i]!=dict2[j]:
						print('введенный тип данных не соответствует заданным анотациям')
						return False
		print(f'введенный тип данный соответствует. Результат:{x(*args,**kwargs)}')	
		return True	
	return wap

@annot
def s(d:int, l:int)->int:
	return d+l
print(s(100,l=400))
print(s('100', l=400))

#задача 5
def kesh(x):
	def wap(*args, **kwargs):
		x1=x(*args, **kwargs)	
		x2=x(*[int(input(f'введите для второго результата: ')) for i in ([*args]+[*kwargs])])
		x3=x(*[int(input('введите число для третьего результата: ')) for j in ([*args]+[*kwargs])])
		return f'сохраненный результат:\n первый: {x1}\n второй: {x2}\n третий:{x3}'	
	return wap
	
@kesh
def s2(d, l):
	return d+l
	
print(s2(int(input('введите число: ')), int(input('введите число: '))))

@kesh
def s3(d, l,c):
	return d+l+c

print(s3(100,200,c=100))


	