# -- coding: utf-8 --
x = 2.444
y = 0.869*(10**(-2))
z = -0.13*(10**3)

import math

a = ((x**(y+1)) + (math.e**(y-1)))
b = (1 + x*(abs(y-math.tan(z))))

o = a / b

c = (1+(abs(y-x)))

d = (( (abs(y-x))**2 ) / 2)
l = (( abs(y-x)**3) / 3)


s = o * c + d - l
print(s)
