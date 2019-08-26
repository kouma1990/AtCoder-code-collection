a, b = (int(i) for i in input().split())

if a==b:
    print(a+b)
else:
    m = max([a,b])
    print(m*2-1)