a, d = (int(i) for i in input().split())

print(max( (a+1)*d, a*(d+1)))