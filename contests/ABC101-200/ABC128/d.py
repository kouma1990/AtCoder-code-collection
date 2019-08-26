import bisect

n,k = (int(i) for i in input().split())
v = [int(i) for i in input().split()]

res = -10**10
for x in range( min(k+1,n+1) ):
    for l in range(x+1):
        r = x-l
        tras = k-x
        get = sorted(v[:l] + (v[-r:] if r!=0 else []))
        
        idx_0 = bisect.bisect_left(get,0)
        if res < sum(get[ min(idx_0,tras) :]):
            res = sum(get[ min(idx_0,tras) :])

print(res)