def average(array):
    result = set(array)
    return sum(result)/len(result)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
