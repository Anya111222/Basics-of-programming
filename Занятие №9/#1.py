# -- coding: utf-8 --
#4-var

#1
def mas():
    A = [[int(i) for i in input().split()], [int(i) for i in input().split()]]
    for i in A:
        for j in i:
            print(j, end = ' ')
        print()
    m = A[0][0] + A[0][1] + A[0][2]
    n = A[1][0] + A[1][1] + A[1][2]
    if m > n:
        return print('Наибольшее:', m, 'Наименьшее:', n)
    else:
        return print('Наибольшее:', n, 'Наименьшее:', m)
mas()