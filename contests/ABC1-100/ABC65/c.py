import math
n,m = (int(i) for i in input().split())
if abs(n-m) > 1:
    print(0)
    exit()

res = math.factorial(n) * math.factorial(m)
if n==m:
    res *= 2
print(res%(10**9+7))
