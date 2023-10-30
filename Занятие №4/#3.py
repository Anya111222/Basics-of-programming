# -- coding: utf-8 --

def main():
    a,b = map(int, input().split())
    if a > b:
        for i in range(a, b + -1, -1):
            if i % 2 != 0:
                print(i)
    else:
        print('Число A должно быть больше чем число B')
            
main()
