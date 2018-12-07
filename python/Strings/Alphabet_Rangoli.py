def print_rangoli(size):
    l = 4*n-3
    alphabets = ' abcdefghijklmnopqrstuvwxyz'
    max_str = '-'.join([alphabets[n-i] for i in range(n)]+[alphabets[i] for i in range(2,n+1)])
    for i in range(n):
        print((max_str[:2*i]+max_str[-2*i-1:]).center(l,'-'))
    for i in range(n-2,-1,-1):
        print((max_str[:2*i]+max_str[-2*i-1:]).center(l,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
