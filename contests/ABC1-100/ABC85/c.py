n, y = (int(i) for i in input().split())


for i in range(n+1):
    if 10000*i + 5000*(n-i) < y:
        continue
    if 10000*i + 1000*(n-i) > y:
        break
    for j in range(n+1-i):
        x = 10000*i + 5000*j + 1000*(n-i-j)
        if x==y:
            print("{} {} {}".format(i, j, n-i-j))
            exit()
print("-1 -1 -1")