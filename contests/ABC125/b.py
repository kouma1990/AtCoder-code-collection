n = int(input())
v = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

res = 0
for i in range(n):
    value = v[i]-c[i]
    if value > 0:
        res+=value

print(res)