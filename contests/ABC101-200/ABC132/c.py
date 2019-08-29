n = int(input())
d = sorted([int(i) for i in input().split()])
print(d[n//2] - d[n//2 - 1])