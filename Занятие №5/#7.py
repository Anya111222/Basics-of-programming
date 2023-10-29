# -- coding: utf-8 --
def main():
    i=1
    n=0
    list=[]
    while i!=0:
        i=int(input())
        list.append(i)
    for x in range(1, len(list)):
        if list[x] > list[x -1]:
            n +=1
    return n
print(main())