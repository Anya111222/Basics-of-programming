# -- coding: utf-8 --
x = 1.825*(10**2)
y = 18.225
z = -3.298*(10**(-2))

import math

a = (abs((x**(y/x)) - ((y/x)**(1/3))) )

b = (y-x)

o = (math.cos(y) - (z/(b)))
p = (1 + ((b)**2))

u = (o/(p))
i = b * u

s = a + i
print(s)