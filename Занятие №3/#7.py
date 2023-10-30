# — coding: utf-8 — 

def main(): 
 N=int(input()) 
 if (N%4==0 and N%100!=0) or N%300==0: 
     return 'Да' 
 else: 
     return 'Нет' 
 
print(main())
