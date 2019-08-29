import math
n, d = (int(i) for i in input().split())
x = [[int(i) for i in input().split()] for i in range(n)]

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        dd = 0
        for d_ in range(d):
            diff = x[i][d_] - x[j][d_]
            dd += diff**2
        if math.sqrt(dd).is_integer():
            cnt += 1

print(cnt)
