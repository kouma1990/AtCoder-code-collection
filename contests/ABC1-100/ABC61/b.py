n,m = (int(i) for i in input().split())
e = [[int(i)-1 for i in input().split()] for i in range(m)]

count = [0]*n

for x in e:
    for y in x:
        count[y] += 1

for x in count:
    print(x)
