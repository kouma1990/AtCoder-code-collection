n, m = (int(i) for i in input().split())
xyz = [[int(i) for i in input().split()] for i in range(n)]

res = 0
for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            l = []
            for x,y,z in xyz:
                l.append(x*i + y*j + z*k)

            res = max(res, abs(sum(sorted(l, reverse=True)[:m])))


print(res)