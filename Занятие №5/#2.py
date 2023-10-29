# -- coding: utf-8 --
def inp():
    N=0
    while N<2:
        N=int(input('N, не меньшее 2 '))
        if N>=2:
            break
        else:
            print('Число не меньше 2')
    return N

def main():
    N = inp()
    for i in range(2, N+1):
        if N%i==0:
            return i
print(main())