from itertools import product

K,M = map(int,input().split())

candidates = list(product(*[list(map(int,input().split()))[1:] for i in range(K)]))
results = list(map(lambda x : sum(i**2 for i in x)%M, candidates))

print(max(results))
