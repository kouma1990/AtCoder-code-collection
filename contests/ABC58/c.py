n = int(input())
s = [input() for i in range(n)]

m = "abcdefghijklmnopqrstuvwxyz"
count = []

for x in m:
    cnt = 100
    for si in s:
        cnt = min(cnt,si.count(x))

    count.append(cnt)

res = ""
for i in range(26):
    res += m[i]*count[i]

print(res)