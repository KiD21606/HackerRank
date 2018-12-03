import numpy as np

arr = list(map(int, input().rstrip().split()))
N = arr[0]
M = arr[1]
P = arr[2]

array_1 = []
for i in range(N):
    temp = list(map(int,input().rstrip().split()))
    array_1.append(temp)

array_2 = []
for i in range(M):
    temp = list(map(int,input().rstrip().split()))
    array_2.append(temp)

array_1 = np.array(array_1)
array_2 = np.array(array_2)
array = np.concatenate((array_1,array_2),axis = 0)
print(array)
