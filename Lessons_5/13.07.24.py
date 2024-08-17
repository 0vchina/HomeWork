#задание 5
s=[1, 2, 67, 69, 98]
print([x**2 for x in s])
print([x%11 for x in s])
print([x for x in s if x%2==0])
print([x for x in s if len(str(x))%2==0])
print([x for x in s if s.index(x)%3!=0])
#задание 1
a=input('введите букву:')
match a:
	case 'a' | 'e' | "u" | "i" |"o"|"y":
		print ("гласная")
	case _:
		print("не гласная или не буква")
#задание 2
a=input("введите день недели:")
match a:
	case  "monday" | "tuesday" |"wednesday"|"thursday"| "friday": 
		print("рабочий день")
	case "saturday"|"sunday":
		print ("нерабочий день")
	case _:
		print('нет такого дня')
#задание 3
a=input("введите фрукт:")
match a:
	case  "лимон": 
		print("желтый")
	case "апельсин":
		print ("оранжевый")
	case _:
		print('нет такого фрукта')
#задание 4
a=input("введите оценку:")
match a:
	case  '1': 
		print("очень плохо")
	case '2':
		print ("плохо")
	case '3':
		print ("удовлетворительно")
	case '4':
		print ("хорошо")
	case '5':
		print ("отлично")	
	case _:
		print('нет такой оценки')