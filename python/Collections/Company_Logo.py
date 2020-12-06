if __name__ == '__main__':
    s = input()
    d = {}
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]]-=1
        else:
            d[s[i]]=-1
    counts = [(d[key],key) for key in d.keys()]
    counts.sort()
    print(counts[0][1],-counts[0][0])
    print(counts[1][1],-counts[1][0])
    print(counts[2][1],-counts[2][0])
