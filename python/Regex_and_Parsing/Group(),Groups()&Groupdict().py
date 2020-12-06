'''
def fun(S):
    for i in range(len(S)-1):
        if S[i].isalnum():
            if S[i]==S[i+1]:
                return S[i]
    return -1

S = input()
print(fun(S))
'''
import re
S = input()
m = re.search(r'([0-9a-zA-Z])\1+', S)
if m:
    print(m.group(1))
else:
    print(-1)
