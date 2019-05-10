import bisect

n = int(input())
a = sorted([int(i) for i in input().split()])

idx = bisect.bisect_right(a,0)

res = -sum(a[:idx]) + sum(a[idx:])

if idx%2==1:
    if idx<n:
        c = min(abs(a[idx-1]), abs(a[idx]))
        res -= 2*c
    else:
        res -= 2*abs(a[idx-1])
        
print(res)
