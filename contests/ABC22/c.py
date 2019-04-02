import copy
n, m = (int(i) for i in input().split())
uvl = [[int(i) for i in input().split()] for i in range(m)]

mat = [[0 for i in range(n)] for j in range(n)]
inf = 10**10
for u,v,l in uvl:
    mat[u-1][v-1] = l
    mat[v-1][u-1] = l

def f(idx, arr, cost):
    used = copy.copy(arr)
    if used[0] == 1:
        return cost

    l = []
    for i,x in enumerate(mat[idx]):
        if used.count(1) == 1 and i==0:
            continue
        if x > 0 and used[i] == 0:
            used[i] = 1
            l.append(f(i, used, cost+x))
            used[i] = 0
    if len(l) == 0:
        return inf
    return min(l)

res = f(0,[0]*n,0)

if res == inf:
    print(-1)
else:
    print(res)