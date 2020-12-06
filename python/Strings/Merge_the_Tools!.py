def merge_the_tools(string, k):
    l = len(string)
    n = int(l/k)
    for i in range(n):
        strs = ''
        alphabets = set()
        for j in range(i*k,(i+1)*k):
            if not string[j] in alphabets:
                strs += string[j]
                alphabets |= {string[j]}
        print(strs)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
