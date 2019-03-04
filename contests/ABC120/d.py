# UnionTreeクラス：グループ分けを木構造で管理する
class UnionFind():
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.N = N

    # xのrootを返す
    def root(self, x):
        return x if self.par[x] == x else self.root(self.par[x])

    # x, yが同じrootの場合true
    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

    # x,yのrootが違った場合、併合
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if(rx != ry):
            for i in range(self.N):
                if self.par[i] == rx:
                    self.par[i] = ry

def output(uf):
    count = 0
    for i in range(uf.N):
        sub_par = uf.par[i+1:]
        count += len(sub_par) - sub_par.count(uf.par[i])

    return count



n, m = (int(i) for i in input().split())
input_arr = [[int(i) for i in input().split()] for i in range(m)] 

uf = UnionFind(n)
#input_arr = [[1,2],[3,4],[1,3],[2,3],[1,4]]

#print(output(uf))
result = [output(uf)]
for i in input_arr[::-1]:
    a = i[0]-1
    b = i[1]-1
    uf.unite(a,b)
    result.append(output(uf))
    #print(output(uf))
    #print("{},{}:{}:{}".format(a, b, uf.par, output(uf) ))

for i in result[::-1][1:]:
    print(i)

#print(uf.par)
