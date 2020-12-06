from collections import OrderedDict
N = int(input())
ord_dic = OrderedDict()
for _ in range(N):
    item, space, price = input().rpartition(' ')
    ord_dic[item] = ord_dic.get(item, 0) + int(price)

for item in ord_dic:
    print(item, ord_dic[item])
