import re

vowels = 'aeiouAEIOU'
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
ans = re.findall('(?<=[%s])[%s]{2,}(?=[%s])' % (consonants,vowels,consonants), input())
if ans:
    print(*ans, sep='\n')
else:
    print(-1)
