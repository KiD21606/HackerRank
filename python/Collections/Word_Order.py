from collections import OrderedDict
N = int(input())
ord_dic = OrderedDict()
for _ in range(N):
    word = input()
    ord_dic[word] = ord_dic.get(word, 0) + 1

print(len(ord_dic))
print(*ord_dic.values())
