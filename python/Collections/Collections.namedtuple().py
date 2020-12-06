from collections import namedtuple

N = int(input())
args = input().split()
students = namedtuple('students',args)
score = 0
for _ in range(N):
    temp = students(*input().split())
    score += int(temp.MARKS)
print('%.2f' % (score/N))
