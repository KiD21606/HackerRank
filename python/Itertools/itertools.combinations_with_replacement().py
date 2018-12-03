from itertools import combinations_with_replacement

task = input().split()
string = sorted(list(task[0]))
k = int(task[1])

for item in combinations_with_replacement(string, k):
    print(''.join(item))
