h, w = (int(i) for i in input().split())
e = [[int(i) for i in input().split()] for i in range(h)]

res = []
for j in range(h)[::2]:
    for i in range(w):
        if e[j][i] % 2 == 1:
            if i < w-1:
                e[j][i+1] += 1
                res.append("{} {} {} {}".format(j+1, i+1, j+1, i+2))
            else:
                if j<h-1:
                    e[j+1][i] += 1
                    res.append("{} {} {} {}".format(j+1, i+1, j+2, i+1))

    if j+1 >= h:
        break

    for i in range(w)[::-1]:
        if e[j+1][i] % 2 == 1:
            if 0 < i:
                e[j+1][i-1] += 1
                res.append("{} {} {} {}".format(j+2, i+1, j+2, i))
            else:
                if j+1<h-1:
                    e[j+2][i] += 1
                    res.append("{} {} {} {}".format(j+2, i+1, j+3, i+1))

print(len(res))
for x in res:
    print(x)

