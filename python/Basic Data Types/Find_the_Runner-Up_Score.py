if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    win = [-100,-100]

    for i in range(n):
        if arr[i]>win[1]:
            if arr[i]>win[0]:
                win[0],win[1] = arr[i],win[0]
            elif arr[i]<win[0]:
                win[1] = arr[i]
    print(win[1])
