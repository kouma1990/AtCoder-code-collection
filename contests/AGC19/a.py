q, h, s, d = (int(i) for i in input().split())
n = int(input())

h = min(q*2, h)
s = min(h*2, s)
d = min(s*2, d)

res = d*(n//2)+s*(n%2)
print(res)

