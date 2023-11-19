# -- coding: utf-8 --

def main():
    a,b = map(int, input().split())
    if a<b:
        for i in range(a,b+1):
            print(i)
    elif a>b:
        for i in range(a,b-1, -1):
            print(i)

main()
