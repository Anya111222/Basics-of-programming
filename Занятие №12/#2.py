# -- coding: utf-8 --

#БлокБ
#2
def find_second_largest():
    n = int(input())
    if n == 0:
        return -1, -1
    max1, max2 = find_second_largest()
    if n > max1:
        return n, max1
    elif n > max2:
        return max1, n
    else:
        return max1, max2

max1, max2 = find_second_largest()
print(max2)