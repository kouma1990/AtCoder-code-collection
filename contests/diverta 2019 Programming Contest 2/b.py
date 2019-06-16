n = int(input())
xy = [[int(i) for i in input().split()] for i in range(n)]

if n == 1:
    print(1)
    exit()
dic = {}
for x1,y1 in xy:
    for x2,y2 in xy:
        if x1 == x2 and y1 == y2:
            continue
        dx = x2 - x1
        dy = y2 - y1
        key = "{},{}".format(dx,dy)
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1

for k, v in sorted(dic.items(), key=lambda x: -x[1]):
    print(n-v)
    break