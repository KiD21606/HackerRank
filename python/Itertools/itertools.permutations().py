from itertools import permutations

task = input().split()
S = sorted(list(task[0]))
k = int(task[1])
for item in permutations(S,k):
    print(''.join(item))
