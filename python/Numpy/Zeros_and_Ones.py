import numpy as np

size = list(map(int,input().rstrip().split()))

zeros = np.zeros(size,dtype = np.int)
ones = np.ones(size,dtype = np.int)

print(zeros)
print(ones)
