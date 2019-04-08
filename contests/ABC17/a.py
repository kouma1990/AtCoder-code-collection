se = [[int(i) for i in input().split()] for i in range(3)]

res = 0
for s,e in se:
    res += (s//10) * e

print(res)