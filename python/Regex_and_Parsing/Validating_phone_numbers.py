'''
A ten digit number starting with a 7, 8 or 9.
'''
import re

for _ in range(int(input())):
    if re.match(r'^[7-9]\d{9}$',input()):
        print('YES')
    else:
        print('NO')
