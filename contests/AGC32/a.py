n = int(input())
b = [int(i) for i in input().split()]

res = []
while True:
    if len(b) == 0:
        break
    flg = True

    for i in range(len(b)):
        k = len(b)-i-1
        if k == b[k]-1:
            a = b.pop(k)
            res.append(a)
            flg = False
            break

    if flg:
        print(-1)
        exit()

for x in res[::-1]:
    print(x)