# -- coding: utf-8 --
def srzer():
    srz = 0
    sum = 0
    A = [int(a) for a in input().split()]
    for a in A:
        sum +=a
    while 0 in A:
            A.remove(0)
    el_cou = len(A)
    w = el_cou
    sum /=w
    return print(sum)
srzer()