# -- coding: utf-8 --
x = 17.421
y = 10.365*(10**(-3))
z = 0.828*(10**5)

import math

a = ((x-1)**(1/3))

b = ((y + a)**0.25)
o = ((abs(x-y)) * ((math.sin(z)**2) + math.tan(z)))

s = b/o
print(s)