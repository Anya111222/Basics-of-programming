# -- coding: utf-8 --
x = -2.235*(10**(-2))
y = 2.23
z = 15.221

import math

a = (math.e**(abs(x-y))) * ( (abs(x-y))**(x+y) )
b = (math.atan(x) + math.atan(z))

o = a / b

p = (x**6) + (math.log(y)**2)
u = (p**(1/3))

s = o + u
print(s)
