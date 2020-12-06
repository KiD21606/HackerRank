def convertion(n,k):
    result = ''
    string = '0123456789ABCDEF'
    while n>0:
        result = string[n%k]+result
        n = n//k
    return result

def print_formatted(n):
    result = ''
    width = 1
    while n >= 2**width:
        width+=1
    for i in range(1,n+1):
        result += str(i).rjust(width)
        result += convertion(i,8).rjust(width+1)
        result += convertion(i,16).rjust(width+1)
        result += convertion(i,2).rjust(width+1)+'\n'
    print(result)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
