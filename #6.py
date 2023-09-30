# -- coding: utf-8 --
x = 16.55*(10**(-3))
y = -2.75
z = 0.15

import math

a = (x**(1/3))
b = (x**(y+2))
k = (a+b)

o = (math.sqrt(10*k))

p = (math.asin(z)**2)
u = (abs(x-y))

h = (p - (u))

s = o * h
print(s)
