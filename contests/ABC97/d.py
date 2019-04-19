# UnionTreeクラス：グループ分けを木構造で管理する
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
            return self.root(self.par[x])

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
            

n, m = (int(i) for i in input().split())
a = [int(i)-1 for i in input().split()]
xy = [[int(i)-1 for i in input().split()] for i in range(m)]

uf = UnionFind(n)

for x,y in xy: 
    uf.unite(x, y)

cnt = 0
for idx, a_ in enumerate(a):
    if uf.same(idx, a_):
        cnt += 1

print(cnt)

