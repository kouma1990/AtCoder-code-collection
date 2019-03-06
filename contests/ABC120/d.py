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
input_arr = [[int(i) for i in input().split()] for i in range(m)] 

uf = UnionFind(n)
#input_arr = [[1,2],[3,4],[1,3],[2,3],[1,4]]

#print(output(uf))
result = [int(n*(n-1)/2)]
for i in input_arr[::-1]:
    a = i[0]-1
    b = i[1]-1
    if not uf.same(a,b):
        x = uf.size[uf.root(a)] * uf.size[uf.root(b)]
        uf.unite(a,b)
        result.append(int(result[-1]-x))
    else:
        result.append(result[-1])

for i in result[::-1][1:]:
    print(i)

#print(uf.par)
