import math
import os
import random
import re
import sys

def solve(s):
    n = len(s)
    if 97<=ord(s[0])<=122:
        Name = chr(ord(s[0])-32)
    else:
        Name = s[0]
    for i in range(n-1):
        if s[i]==' ' and 97<=ord(s[i+1])<=122:
            Name += chr(ord(s[i+1])-32)
        else:
            Name += s[i+1]
    return Name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
