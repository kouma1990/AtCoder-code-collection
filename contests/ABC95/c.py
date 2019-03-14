a, b, c, x, y = [int(i) for i in input().split()]

cost = 0
if a+b > c*2:
    min_xy = min(x,y)
    cost += c*2*min_xy
    x -= min_xy
    y -= min_xy
    
cost += c*2*x if a > c*2 else a*x
cost += c*2*y if b > c*2 else b*y

print(cost)