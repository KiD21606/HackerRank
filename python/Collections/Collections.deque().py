from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    cmd = input().split()
    if len(cmd)==1:
        eval('d.'+cmd[0]+'()')
    else:
        eval('d.'+cmd[0]+'('+cmd[1]+')')

print(*d)
