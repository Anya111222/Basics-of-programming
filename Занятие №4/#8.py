# -- coding: utf-8 --
N=int(input())
for i1 in range(1, N+1):
    for i2 in range(1, i1+1):
        print(i2, sep='', end='')
    print()