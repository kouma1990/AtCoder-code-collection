n = int(input())
p = [int(i) for i in input().split()]

res = 0
for i in range(1,n-1):
    a = sorted([p[i-1], p[i], p[i+1]])
    if a[1] == p[i]:
        res+=1

print(res)