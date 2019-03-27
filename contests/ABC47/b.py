w,h,n = (int(i) for i in input().split())
xya = [[int(i) for i in input().split()] for i in range(n)]

sx = 0
sy = 0
ex = w
ey = h
for x,y,a in xya:
    if a == 1:
        sx = max(sx,x)
    if a == 2:
        ex = min(ex,x)
    if a == 3:
        sy = max(sy,y)
    if a == 4:
        ey = min(ey,y)

if ex-sx > 0 and ey-sy > 0:
    print((ex-sx)*(ey-sy))
else:
    print(0)
