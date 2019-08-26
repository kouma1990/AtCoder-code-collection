import collections
n = int(input())
s = input()

c = collections.Counter(s)

res = 1
for x in c.values():
    res *= (x+1)

print( (res-1) % (10**9 + 7))