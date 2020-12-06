from collections import Counter

input()
shoes = Counter(map(int,input().split()))
income = 0
for _ in range(int(input())):
    size, price = map(int,input().split())
    if shoes[size] > 0:
        shoes[size] -= 1
        income += price
print(income)
