'''
tourists = set()
families = set()
input()
rooms = input().split()

for room in rooms:
    if room in tourists:
        families.add(room)
    else:
        tourists.add(room)

for i in tourists-families:
    print(i)
'''
K = int(input())
tourists = list(map(int,input().split()))
rooms = set(tourists)
print((sum(rooms)*K-sum(tourists))//(K-1))
