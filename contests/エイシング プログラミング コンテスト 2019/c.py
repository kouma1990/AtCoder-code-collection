import sys
input = sys.stdin.readline

h, w = (int(i) for i in input().split())
a = [input() for i in range(h)]

class UnionFind():
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.size = [1] * N
        self.N = N

    # xのrootを返す
    def root(self, x):
        if self.par[x] == x:
            return x
        else: 
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # x, yが同じrootの場合true
    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

    # x,yのrootが違った場合、併合
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if self.size[rx] < self.size[ry]:
            self.par[rx] = ry
            self.size[ry] += self.size[rx]
        else:
            self.par[ry] = rx
            self.size[rx] += self.size[ry]
            
uf = UnionFind(h*w)

for j in range(h):
    for i in range(w):
        if i != w-1 and a[j][i+1] != a[j][i]:
            uf.unite(w*j+i,w*j+i+1)
        if j != h-1 and a[j+1][i] != a[j][i]:
            uf.unite(w*j+i,w*(j+1)+i)

for v in range(h*w):
    uf.root(v)

wc = [0]*(h*w)
bc = [0]*(h*w)
for j in range(h):
    for i in range(w):
        idx = w*j+i
        if a[j][i] == ".":
            wc[uf.par[idx]] += 1
        else:
            bc[uf.par[idx]] += 1

res = 0
for i in range(h*w):
    res += wc[i] * bc[i]
print(res)
