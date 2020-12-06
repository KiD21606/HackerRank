n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    task = input()
    if task == 'pop':
        s.pop()
    else:
        cmd,k = task.split()
        eval('s.'+cmd+'('+k+')')
print(sum(s))
