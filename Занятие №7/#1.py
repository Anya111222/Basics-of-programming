# -- coding: utf-8 --
#8-var

def sumer():
    p = 1
    s = 0
    A = [int(i) for i in input().split()]
    for a in A:
        s += a
        p *= a
    return print(s,p)
sumer()