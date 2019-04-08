n,m = (int(i) for i in input().split())
ab = [[int(i)-1 for i in input().split()] for i in range(m)]

mat = arr = [[0 for i in range(n)] for j in range(n)]
for a,b in ab:
    mat[a][b] = 1
    mat[b][a] = 1

for i in range(n):
    used = [0]*n
    cnt = 0
    used[i] = 1
    for idx,x in enumerate(mat[i]):
        if idx==i:
            continue
        used[idx] = x

    for idx,x in enumerate(mat[i]):
        if x==1:
            for idx2,xx in enumerate(mat[idx]):
                if xx==1 and used[idx2] == 0:
                    used[idx2] = 1
                    cnt += 1

    print(cnt)
