n = int(input())
v = sorted([int(i) for i in input().split()])

res = v[0]

for x in v[1:]:
    res += x
    res /= 2

print(res)

