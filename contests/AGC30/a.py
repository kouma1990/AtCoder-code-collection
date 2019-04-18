a, b, c = (int(i) for i in input().split())

print(min(b+c, a+b+1+b))
