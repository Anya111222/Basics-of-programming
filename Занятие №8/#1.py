# -- coding: utf-8 --
#3-var

from math import sqrt
def katet():
    a,b = map(int, input('Введите катеты 1-го треугольника: ').split())
    a2, b2 = map(int, input('Введите катеты 2-го треугольника: ').split())
    c = (a**2) + (b**2)
    c2 = (a2**2) + (b2**2)
    if c > c2:
        return print('c =', sqrt(c))
    else: print('c2 =', sqrt(c2))
katet()