#triangle calculation

def triangle_calculation(a,b,c):
    if a+b<c or a+c<b or b+c<a:
        return 'error'
    P=a+b+c
    p=P/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    return P, S

