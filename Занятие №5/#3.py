# -- coding: utf-8 --
n=int(input())
def main(n):
    a=2
    b=1
    while a<=n:
        a*=2
        b+=1
    return(f'Показатель: {b-1}, Степень: {a//2}')
print(main(n))