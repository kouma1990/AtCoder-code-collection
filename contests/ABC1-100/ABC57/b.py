n,m = (int(i) for i in input().split())
ab = [[int(i) for i in input().split()] for i in range(n)]
cd = [[int(i) for i in input().split()] for i in range(m)]

for x1 in ab:
    min_dist = 10**10
    min_idx = 0
    for idx,x2 in enumerate(cd):
        dist = abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])
        if dist < min_dist:
            min_dist = dist
            min_idx = idx
    
    print(min_idx+1)
