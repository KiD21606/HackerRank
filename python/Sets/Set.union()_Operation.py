input()
English = set(map(int,input().split()))
input()
French = set(map(int,input().split()))

print(len(English.union(French)))
