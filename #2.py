# -- coding: utf-8 -
x = -4.5
y = 0.75*(10**-4)
z = -0.845*(10**2)

import math

a = ((x-y)**2)
b = ((9 + a)**(1/3))
c = ((x**2) + (y**2) + 2)
c = (b / c)
l = abs(x-y)
d = (math.e**l)
j = ((math.tan(z))**3)
m = d * j

s = c - m
print(s)