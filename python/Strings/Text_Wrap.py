import textwrap

def wrap(string, n):
    result = ''
    k = len(string)//n
    for i in range(k):
        result += string[n*i:n*(i+1)]+'\n'
    if len(string)%n != 0:
        result += string[n*k:]+'\n'
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
