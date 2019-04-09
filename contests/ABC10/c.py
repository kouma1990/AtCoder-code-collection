sx, sy, ex, ey, t, v = (int(i) for i in input().split())
n = int(input())
xy = [[int(i) for i in input().split()] for i in range(n)]

l = t*v

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

for x, y in xy:
    d1 = dist(sx,sy,x,y)
    d2 = dist(x,y,ex,ey)
    if (d1+d2)<=l:
        print("YES")
        exit()
print("NO")