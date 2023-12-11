# -- coding: utf-8 --
#2
def openfile():
    with open('Занятие_10Бушмакина_Анна_Станиславовна_У-232_vvod_t2.txt','r') as file:
        A = []
        matrix = file.readlines()
        for i in matrix:
            stroke = []
            for j in i.split():
                stroke.append(int(j))
            A.append(stroke)
        file.close()
    return A

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
    M = []
    n = len(A)
    for i in range(n):
        stroke = []
        for j in range(n):
            if i < j:
                stroke.append(0)
                print(0, end=' ')
            else:
                stroke.append(A[i][j])
                print(A[i][j], end=' ')
        M.append(stroke)
        print()
    save(M)

def save(A):
    with open('Занятие_10Бушмакина_Анна_Станиславовна_У-232_vivod_t2.txt','w') as file:
        for i in A:
            out = ' '.join(map(str,i))
            file.write(out+'\n')
        file.close()
            

A = mas(openfile())
mass(A)
