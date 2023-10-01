# -- coding: utf-8 --
N=int(input())
M=int(input())
K=int(input())
if (K<N*M) and ((K%M==0) or (K%N==0)):
    print('YES')
else:
    print('NO')