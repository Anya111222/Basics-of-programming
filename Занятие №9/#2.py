# -- coding: utf-8 --
#4-var

#2
def mas(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] < 0:
                A[i][j] = 0
            else:
                A[i][j] = 1
    return A

def mass(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i < j:
                print(0, end=' ')
            else:
                print(A[i][j], end=' ')
        print()

# Пример использования
A = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
A = mas(A)
mass(A)