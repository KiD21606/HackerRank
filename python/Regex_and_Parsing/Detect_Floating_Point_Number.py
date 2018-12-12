'''
constrains:
1. Consist of numbers, "+", "-", and ".".
2. Contain at most one of "+" and "-".
3. Have exactly one "." symbol, and must have a number after ".".
4. must contain at least 1 decimal value. 
'''

for _ in range(int(input())):
    dot = False
    number = False
    string = input()
    if string[0] in '0123456789':
        number = True
    elif string[0] in '+-':
        pass
    elif string[0] == '.':
        dot = True
    else:
        print(False)
        continue
    
    result = True
    for i in range(1,len(string)):
        if string[i] in '0123456789':
            number = True
        elif string[i] == '.' and dot == False :
            if i+1 == len(string):
                result = False
            elif string[i+1] in '0123456789':
                dot = True
        else:
            result = False
            break
    if number == False or dot == False:
        result = False
    print(result)

'''
import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
'''
'''
^ : start of the expression.

[-+]? : start with either - or +.

[0-9] : any number from 0-9 can be followed after it.

* : the process ([0-9]) can repeat arbitrarily times (even 0 times).

\. : '\' is the skip char that is used for ".".

+ : the process ([0-9]) can repeat arbitrarily times, but atleast one time.

$ : ending symbol.
'''
