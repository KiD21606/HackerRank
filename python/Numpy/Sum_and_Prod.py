import numpy as np

size = list(map(int,input().split()))
mat = []
for i in range(size[0]):
    mat.append(list(map(int,input().split())))

summ = np.sum(mat,axis=0)
prod = np.prod(summ)
print(prod)
