import re

pattern = r'(?<=.)(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[^0-9a-fA-F])'
for _ in range(int(input())):
    m = re.findall(pattern, input())
    if m:
        print(*m,sep='\n')
