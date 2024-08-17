from triangle import triangle_calculation
from cicrle import circle_calculation
from rectangle import rectangle_calculation

def resalt_triangle(a,b,c):
    resalt={'triangle':{'square': triangle_calculation(a,b,c)[1], 'perimetr':triangle_calculation(a,b,c)[0]}}
    return resalt
print(resalt_triangle(2,3,2))

def resalt_circle(r):
    resalt={'circle':{'square': circle_calculation(r)[1], 'perimetr':circle_calculation(r)[0]}}
    return resalt
print(resalt_circle(10))

def resalt_rectangle(a,b):
    resalt={'rectangle':{'square': rectangle_calculation(a,b)[1], 'perimetr':rectangle_calculation(a,b)[0]}}
    return resalt
print(resalt_rectangle(4,10))