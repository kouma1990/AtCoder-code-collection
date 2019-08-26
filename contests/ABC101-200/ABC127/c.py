n,m = (int(i) for i in input().split())
lr = [[int(i) for i in input().split()] for i in range(m)]

max_l = 0
min_r = lr[0][1]

for l,r in lr:
    max_l = max(l,max_l)
    min_r = min(r,min_r)

if min_r-max_l+1 > 0:
    print(min_r-max_l+1)
else:
    print(0)