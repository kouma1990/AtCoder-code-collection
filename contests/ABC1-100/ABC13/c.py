n,h = (int(i) for i in input().split())
a,b,c,d,e = (int(i) for i in input().split())

min_cost = 10**20
for i in range(n+1):
    ld = n-i
    x = h+b*i+d*ld
    k = min((x-1)//(d+e), ld)
    j = ld-k
    cost = a*i + c*j
    if h+b*i+d*j-e*k>0:
        min_cost = min(cost, min_cost)

print(min_cost)

