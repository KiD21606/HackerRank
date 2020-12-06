n,m = map(int,input().split())
goals = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

happiness = 0
for i in range(n):
    if goals[i] in A:
        happiness += 1
    if goals[i] in B:
        happiness -= 1
print(happiness)
