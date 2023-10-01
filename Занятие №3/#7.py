# -- coding: utf-8 --
y = int(input())
if y%4==0 and y%100!=0 and y%400==0:
    print('Нет')
else:
    print('Да')