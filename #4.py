# -- coding: utf-8 -
x = 0.4*(10**4)
y = -0.875
z = (-0.475*(10**3))
import math
a = math.cos(x)
r = math.cos(y)
p = a - r
q = abs(p)
u = (math.sin(y)**2)
b = (1+2*u)
n = q**b
c = z**2
d = z**3
e = z**4
k = (c/2)
l = (d/2)
m = (e/2)
f = 1 + z + (k) + (l) + (m)
s = q * f
print(s)