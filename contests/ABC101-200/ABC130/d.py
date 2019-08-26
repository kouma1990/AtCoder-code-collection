import bisect
n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

l = [0]
res = 0
for x in a:
    res+=x
    l.append(res)

cnt = 0
for x in l[::-1]:
    if x < k:
        break
    y = bisect.bisect_right(l,x-k)
    cnt += y
print(cnt)