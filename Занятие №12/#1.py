# -- coding: utf-8 --

#БлокА
#3 
def number(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(number(n // 10)))

num = int(input("Введите число: "))
print(number(num))