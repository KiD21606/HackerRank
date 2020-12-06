for _ in range(int(input())):
    input()
    A = set(input().split())
    input()
    B = set(input().split())
    if A-B == set():
        print(True)
    else:
        print(False)
