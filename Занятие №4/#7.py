# -- coding: utf-8 --
N=int(input())
F=1
sum = 0
for i in range(1, N+1):
    F*=i
    sum+=F
print(sum)