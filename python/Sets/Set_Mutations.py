input()
A = set(map(int,input().split()))

for _ in range(int(input())):
    cmd = input().split()[0]
    B = set(map(int,input().split()))
    eval('A.'+cmd+'(B)')

print(sum(A))
