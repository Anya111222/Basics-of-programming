# — coding: utf-8 — 

def nums(): 
 i=int(input()) 
 if i >= 1 and i <= 8: 
     return i 
 else: 
     print('Неправильное число') 
     return nums() 
def main(): 
 X=nums() 
 Y=nums() 
 Z=nums() 
 W=nums() 
 if (X+Y+Z+W)%2==0: 
     return 'Да' 
 else: 
     return 'Нет' 
 
print(main())
