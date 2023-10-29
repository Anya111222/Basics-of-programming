# -- coding: utf-8 --
def main():
    i=1
    x=1
    y=1
    list=[]
    while i!=0:
        i=int(input())
        list.append(i)
    for n in range(1, len(list)):
        if list[n] == list[n-1]:
            x +=1
        else:
            x=1
        if x>y:
            y=x
    return y
print(main())