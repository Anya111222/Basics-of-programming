# -- coding: utf-8 --
a = int(input())
b = int(input())
c = int(input())
v = 0
if a==b and a==c and b==a and b==c and c==a and c==b:
            print(3)
elif a!=b and a!=c and b!=a and b!=c and c!=a and c!=b:
    print(0)
else:
    print(2)