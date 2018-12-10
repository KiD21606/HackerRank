input()
A = set(map(int,input().split()))
input()
B = set(map(int,input().split()))

dif = list(A.difference(B))+list(B.difference(A))
dif.sort()
for i in dif:
    print(i)
