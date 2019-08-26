import copy
n, m = (int(i) for i in input().split())
e = [[int(i)-1 for i in input().split()] for i in range(m)]

b = arr = [[0 for i in range(n)] for j in range(n)]

for x in e:
    b[x[0]][x[1]] = 1
    b[x[1]][x[0]] = 1

def f(idx):
    used[idx] = 1
    for i in range(n):
        if b_[idx][i] == 1 and used[i] == 0:
            f(i)

count = 0
for x in e:
    b_ = copy.deepcopy(b)
    b_[x[0]][x[1]] = 0
    b_[x[1]][x[0]] = 0
    used = [0]*n
    f(0)
    if used.count(1) != n:
        count+=1

print(count)

