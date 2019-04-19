n, m = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

acc = 0
l = []
for x in a:
    acc += x
    l.append(acc%m)

dic = {}
res = 0
for x in l:
    if x in dic:
        res += dic[x]
        dic[x] += 1
    else:
        dic[x] = 1

    if x == 0:
        res += 1


print(res)

