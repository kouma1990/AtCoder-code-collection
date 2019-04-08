n, m = (int(i) for i in input().split())
xyr = [[int(i) for i in input().split()] for i in range(n)]
xy = [[int(i) for i in input().split()] for i in range(m)]

def dist(x0,y0,x1,y1):
    return ( (x0-x1)**2 + (y0-y1)**2 )**0.5

r = [10**10]*m

for i,a in enumerate(xy):
    x0 = a[0]
    y0 = a[1]
    for x1,y1,r1 in xyr:
        d = dist(x0,y0,x1,y1)
        r[i] = min(r[i],d-r1)

    for x1,y1 in xy:
        if x0==x1 and y0==y1:
            continue

        d = dist(x0,y0,x1,y1)
        r[i] = min(r[i], d/2)

cr = list(map(lambda x:x[2],xyr))
if len(r) == 0:
    print(min(cr))
elif len(cr) == 0:
    print(min(r))
else:
    print(min( min(r), min(cr) ))