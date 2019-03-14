# 1行に1つの数字
n = int(input())
a = [input() for i in range(n)]

cnt = [0]*5

for x in a:
    if x[0] == "M": cnt[0] += 1
    if x[0] == "A": cnt[1] += 1
    if x[0] == "R": cnt[2] += 1
    if x[0] == "C": cnt[3] += 1
    if x[0] == "H": cnt[4] += 1
    
count = 0
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1,5):
            count += cnt[i]*cnt[j]*cnt[k]

print(count)