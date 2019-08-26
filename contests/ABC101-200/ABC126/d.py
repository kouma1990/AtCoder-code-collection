import sys
input = sys.stdin.readline

n = int(input())
uvw = []
e = {}
for i in range(n-1):
    x = input().split()
    uvw.append([int(x[0])-1, int(x[1])-1, int(x[2])%2])
    e[i] = []
e[n-1] = []

w_mat = [[0 for i in range(n)] for j in range(n)]
for u,v,w in uvw:
    if w%2:
        e[u].append(v)
        e[v].append(u)
        w_mat[u][v] = w
        w_mat[v][u] = w

res = [0]*n
used = [0]*n

def f(idx, pre_idx):
    if w_mat[idx][pre_idx]:
        res[idx] = int(not res[pre_idx])
    for i in e[idx]:
        if not used[i]:
            used[idx] = 1
            f(i, idx)

for i in range(n):
    if not used[i]:
        used[i] = 1
        f(i,i)

for x in res:
    print(x)

