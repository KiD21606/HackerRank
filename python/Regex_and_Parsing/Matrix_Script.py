import re

n, m = map(int, input().split())

string = [' '] * (n*m)
for j in range(n):
    s = input()
    for i in range(len(s)):
        string[j+i*n] = s[i]

decode = ''.join(string)

print(re.sub(r'(?<=[a-zA-Z0-9])([ !@#$%&]+)(?=[a-zA-Z0-9])', ' ', decode))
