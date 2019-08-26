n,k = (int(i) for i in input().split())
r = sorted([int(i) for i in input().split()])

res = 0
for x in r[n-k:]:
    res = (res+x)/2
print(res)