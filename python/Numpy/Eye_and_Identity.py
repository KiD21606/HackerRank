import numpy as np

size = list(map(int,input().rstrip().split()))
mat = np.eye(size[0],size[1],k=0)
print(str(mat).replace('1',' 1').replace('0',' 0'))
