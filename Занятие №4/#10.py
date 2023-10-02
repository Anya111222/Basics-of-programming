# -- coding: utf-8 --
n=int(input())
k=int(input())
def F(n):
   if n==1 or n==2:
       return 1
   else:
       return F(n-2)+F(n-1)
print((F(n+2)-1)[k-1:])