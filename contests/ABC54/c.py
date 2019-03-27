n,m = (int(i) for i in input().split())
e = sorted([[int(i)-1 for i in input().split()] for i in range(m)])

g = [[0 for i in range(n)] for j in range(n)]
for x in e:
    g[x[0]][x[1]] = 1
    g[x[1]][x[0]] = 1

import copy
count = 0
def f(idx, arr):
    used = copy.copy(arr)
    global count
    used[idx] = 1
    if used.count(0) == 0:
        count += 1

    for i, x in enumerate(g[idx]):
        if x==1 and used[i]==0:
            f(i, used)

used = [0]*n
f(0, used)

print(count)
