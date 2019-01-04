import re

def varify(s):
    if not re.match(r'^[456]\d{3}(-?\d{4}){3}$',s):
        return 'Invalid'
    s = s.replace('-','')
    if re.search(r'(\d)\1{3}',s):
        return 'Invalid'
    return 'Valid'
    
for _ in range(int(input())):
    print(varify(input()))
