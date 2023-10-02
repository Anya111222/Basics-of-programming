# -- coding: utf-8 --
n=int(input())
nn=[0, 1]
for i in range(2, n+1):
    nn.append(nn[i-1] + nn[i-2])
print(sum(nn))