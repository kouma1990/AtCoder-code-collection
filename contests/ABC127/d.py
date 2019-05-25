# 高速版input
import sys
input = sys.stdin.readline

n,m = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
bc = [[int(i) for i in input().split()] for i in range(m)]

x = []
for b,c in sorted(bc, key=lambda x: x[1], reverse=True):
    x.extend([c]*b)
    if len(x) > n:
        break
        
a.extend(x)
print(sum(sorted(a,reverse=True)[:n]))


"""
# 二分探索
import bisect

n,m = (int(i) for i in input().split())
a = sorted([int(i) for i in input().split()])
bc = [[int(i) for i in input().split()] for i in range(m)]

for b,c in bc:
    idx = bisect.bisect_left(a,c)
    a = (a[:idx] + [c]*b + a[idx:])[b:]

print(sum(a))

"""