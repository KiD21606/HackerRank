A = set(input().split())
result = True
for _ in range(int(input())):
    B = set(input().split())
    if B-A != set() or A-B == set():
        result = False
        break
print(result)
