X = int(input().split()[1])

scores = []
for _ in range(X):
    scores.append(list(map(float,input().split())))

for person in zip(*scores):
    print(sum(person)/X)
