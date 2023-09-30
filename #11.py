# -- coding: utf-8 --
x = 6.251
y = 0.827
z = 25.001

import math

a = ( y**(abs(x)**(1/3)) )

b = (math.cos(y)**3)

o = abs(x - y) * ( 1 + ( (math.sin(z)**2) / (math.sqrt(x+y)) ) )
p = ((math.e**(abs(x-y))) + (x/2))

u = o/p

i = b*u

s = a + i
print(s)