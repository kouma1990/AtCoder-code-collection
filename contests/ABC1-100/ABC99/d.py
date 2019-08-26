import collections
n, c = (int(i) for i in input().split())
d = [[int(i) for i in input().split()] for i in range(c)]
t = [[int(i)-1 for i in input().split()] for i in range(n)]

l = [[],[],[]]
for i in range(n):
    for j in range(n):
        l[(i+j)%3].append(t[j][i])
l = list(map(lambda x: collections.Counter(x), l))

min_cost = n*n*10**5
for i in range(c):
    for j in range(c):
        if j == i:continue
        for k in range(c):
            if k==j or k==i:continue
            cost = 0
            for idx, done in enumerate([i,j,k]):
                for pre, cnt in l[idx].items():
                    cost += d[pre][done] * cnt
            min_cost = min(min_cost, cost)
            
print(min_cost)