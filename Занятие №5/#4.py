# -- coding: utf-8 --
x = int(input())
y = int(input())

def fx(x):
    percent = (x/100)*10
    x+=percent
    return x

def days(x,y):
    days=0
    while x<=y:
        x=fx(x)
        days +=1
    return days

print(days(x,y))