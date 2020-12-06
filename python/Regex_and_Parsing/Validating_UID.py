import re

def check_UID(s):
    if not re.search(r'^[a-zA-Z0-9]{10}$', s):
        return 'Invalid'
    if not re.search(r'[0-9].*?[0-9].*?[0-9]', s):
        return 'Invalid'
    if not re.search(r'[A-Z].*?[A-Z]', s):
        return 'Invalid'
    if len(set(s))<10:
        return 'Invalid'
    return 'Valid'

for _ in range(int(input())):
    print(check_UID(input()))
