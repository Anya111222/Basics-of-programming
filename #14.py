# -- coding: utf-8 --
x = 12.3*(10**(-1))
y = 15.4
z = 0.252*(10**3)

import math

a = (y**(x+1))
b = ((abs(y-2)**(1/3)) + 3)

o = a / b

c = (x + (y/2))
d = (2 * abs(x+y))

l = c/d

i = ((x+1)**(-1/math.sin(z)))

s = o + l * i
print(s)