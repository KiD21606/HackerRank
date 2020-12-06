from itertools import combinations

task = input().split()
string = sorted(list(task[0]))
k = int(task[1])

for i in range(1,k+1):
    for item in combinations(string,i):
        print(''.join(item))
