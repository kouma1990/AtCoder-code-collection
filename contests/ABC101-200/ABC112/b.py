n, t = (int(i) for i in input().split())  
e = [[int(i) for i in input().split()] for i in range(n)] 

min_cost = 100000

for x in e:
    if x[1] <= t and x[0] < min_cost:
        min_cost = x[0]

if min_cost == 100000:
    print("TLE")
else:
    print(min_cost)