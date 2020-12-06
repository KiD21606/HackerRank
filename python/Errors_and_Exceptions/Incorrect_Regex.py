import re

for _ in range(int(input())):
    try:
        reg = re.compile(input())
    except re.error:
        print(False)
    else:
        print(True)
