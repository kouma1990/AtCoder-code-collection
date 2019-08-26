n,x = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

cnt = 0
if a[0] > x:
    cnt += a[0] - x
    a[0] -= cnt

for i in range(1,n):
    c = a[i] + a[i-1] - x
    if c > 0:
        cnt += c
        a[i] -= c


print(cnt)