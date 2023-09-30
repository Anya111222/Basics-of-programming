# -- coding: utf-8 -
x = 3.74*(10**(-2))
y = -0.825
z = 0.16*(10**2)

import math

a = (1 + (math.sin(x+y)**2))
b = 2*y  
k = ( 1 + ( (x**2) * (y**2)) )
o = (b/(k))
c = (abs(x - (o)))
p = (a / (c))
l = (x ** (abs(y)))
d = (p * l)
j = (math.cos( math.atan( (1/(z))) )**2)

s = d + j
print(s)