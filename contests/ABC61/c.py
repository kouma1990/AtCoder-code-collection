n,k= (int(i) for i in input().split())
ab = sorted([[int(i) for i in input().split()] for i in range(n)])

count = 0
for x in ab:
    count += x[1]
    if k <= count:
        print(x[0])
        break
