n, q = (int(i) for i in input().split())
lrt = [[int(i) for i in input().split()] for i in range(q)]

a = [0]*n

for l,r,t in lrt:
    a[l-1:r] = [t]*(r-l+1)

for x in a:
    print(x)