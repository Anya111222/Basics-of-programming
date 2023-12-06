# -- coding: utf-8 --
#1
def openfile():
    with open('import.txt','r') as file:
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
    for i in A:
        for j in i:
            print(j, end = ' ')
        print()
    m = A[0][0] + A[0][1] + A[0][2]
    n = A[1][0] + A[1][1] + A[1][2]
    if m > n:
        return f'Наибольшее: {m}, Наименьшее: {n}'
    else:
        return f'Наибольшее: {n}, Наименьшее: {m}'

def save(data):
    with open('save.txt','w') as file:
        file.write(data)
        file.close()

output = mas(openfile())
save(output)
print(output)
