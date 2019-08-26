import bisect

n = int(input())
x = list(map(lambda x:x*x, list(range(40000))))

idx = bisect.bisect_right(x,n)
print(x[idx-1])