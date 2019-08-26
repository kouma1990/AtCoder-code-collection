import collections
import math

n = int(input())
a = [int(i) for i in input().split()]

l = [0]
for x in a:
    l.append(l[-1]+x)

l = l[1:]

c = collections.Counter(l)

res = 0
for x in c.values():
    res += sum(range(x))

res += c[0]

print(res)
