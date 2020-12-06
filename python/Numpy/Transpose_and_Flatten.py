import numpy
arr = list(map(int, input().rstrip().split()))
N = arr[0]
M = arr[1]
mat = []
for row in range(N):
    mat.append(list(map(int, input().rstrip().split())))
mat = numpy.array(mat)
print(numpy.transpose(mat))
print(mat.flatten())
