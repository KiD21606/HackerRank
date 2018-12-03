from itertools import groupby
for key, group in groupby(input()):
    print(str((len(list(group)),int(key))),end=' ')

'''
# Solve this problem without using groupby.
S = input()
n = len(S)

l = []
integer = S[0]
count = 1
i = 1
while i<n:
    if S[i] == integer:
        count += 1
        i += 1
    else:
        l.append(str(tuple([count,int(integer)])))
        integer = S[i]
        count = 1
        i += 1
l.append(str(tuple([count,int(integer)])))

print(' '.join(l))
'''
