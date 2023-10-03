# — coding: utf-8 — 
def main(): 
 a=int(input()) 
 b=int(input()) 
 l=int(input()) 
 N=int(input()) 
 K=(2 * l + (2 * N - 1) * a + 2 * (N - 1) * b) 
       return(f'Искомая длина шнурка: {K}') 
print(main())