a, b, c, d = (int(i) for i in input().split())

print(max(min(b,d)-(max(a,c)), 0))