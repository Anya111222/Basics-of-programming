# -- coding: utf-8 --
x = 0.1722
y = 6.33
z = 3.25*(10**(-4))

import math

a = 5*(math.atan(x))

b = ((0.25)*(math.acos(x)))

o = ((x + (3*abs(x-y))) + (x**2))
p = (abs(x-y)*z + (x**2))

u = (o / (p))
k = b * u

s = a - k
print(s)