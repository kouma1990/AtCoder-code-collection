n, x = (int(i) for i in input().split())
m = [int(input()) for i in range(n)]

count = len(m)
x -= sum(m)

count+= x//min(m)
print(count)