# -- coding: utf-8 --
N=int(input())
def main(N):
    for i in range(N):
        if i**2<=N:
            print(i**2)
main(N)