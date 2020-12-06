import re

S = input()
k = input()
result = []
m = re.search(k,S)
index = 0
while m!= None:
    result.append((m.start()+index,m.end()+index-1))
    index += m.start()+1
    m = re.search(k,S[index:])

if result == []:
    print((-1,-1))
else:
    print(*result, sep='\n')
