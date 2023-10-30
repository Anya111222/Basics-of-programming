# — coding: utf-8 — 

def main(): 
 X=int(input()) 
 Y=int(input()) 
 Z=int(input()) 
 if X==Y==Z: 
      return 3 
 elif X==Y or Y==Z or X==Z: 
      return 2 
 else: 
      return 0 
print(main())
