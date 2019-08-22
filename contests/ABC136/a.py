a, b, c = (int(i) for i in input().split())

if a >= b+c:
    print(0)
    exit()
else:
    print(b+c-a)