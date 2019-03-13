n, m, q = (int(i) for i in input().split())  
M = [[int(i)-1 for i in input().split()] for i in range(m)]
Q = [[int(i)-1 for i in input().split()] for i in range(q)]

x = [[0 for i in range(n)] for j in range(n)]

for m_ in M:
    x[m_[0]][m_[1]] += 1

c = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0:
            c[i][j] = x[i][j]
        else:
            c[i][j] = c[i][j-1] + x[i][j]

for q_ in Q:
    sum_num = 0
    for i in range(q_[0], q_[1]+1):
        sum_num += c[i][q_[1]] - (c[i][q_[0]-1] if q_[0] > 0 else 0)
    print(sum_num)
