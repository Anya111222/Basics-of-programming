# — coding: utf-8 — 

def main(): 
 N=int(input()) 
 M=int(input()) 
 K=int(input()) 
 if K<N*M and (K%N==0 or K%M==0): 
     return 'Да' 
 else: 
     return 'Нет' 
print(main())
