from math import e

def f(x):
    return e**x

x1 = -1
x2 = 1
n = 10
h = (x2-x1)/n   
S = h* (f(x1) + f(x2))    
for i in range(1,n):
    S+=f(x1+i*h)
Integral = h*S
print('Integral = %.1f' %Integral)