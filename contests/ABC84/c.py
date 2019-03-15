import math
n = int(input())
e = [[int(i) for i in input().split()] for i in range(n-1)]

result = []
for i in range(n-1):
    t = e[i][0] + e[i][1]
    for x in e[i+1:]:
        if t <= x[1]:
            t = x[0] + x[1]
            continue
        t = math.ceil((t-x[1])/x[2])*x[2] + x[1] + x[0]
    result .append(t)

result.append(0)
for x in result:
    print(x)