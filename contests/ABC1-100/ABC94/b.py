import bisect
n, m, x = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

y = bisect.bisect_left(a,x)
print(min(y,len(a)-y))
