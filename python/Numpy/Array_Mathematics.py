import numpy as np

arr = list(map(int,input().rstrip().split()))
N = arr[0]
M = arr[1]

A = []
for i in range(N):
    A.append(list(map(int,input().rstrip().split())))
A = np.array(A)
B = []
for i in range(N):
    B.append(list(map(int,input().rstrip().split())))
B = np.array(B)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
