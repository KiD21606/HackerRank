from itertools import combinations

N = int(input())
string = sorted(list(input().split()))
K = int(input())

num0 = len(list(combinations(string,K)))

i=0
while i<N:
    if string[i]!='a':
        break
    else:
        i+=1

if N-i<K:
    num1 = 0
else:
    num1 = len(list(combinations(string[i:],K)))
print(1-num1/num0)
