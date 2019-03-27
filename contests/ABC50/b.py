n = int(input())
t = [int(i) for i in input().split()]
m = int(input())
px = [[int(i) for i in input().split()] for i in range(m)]

s = sum(t)
for p,x in px:
    print(s-t[p-1]+x)
