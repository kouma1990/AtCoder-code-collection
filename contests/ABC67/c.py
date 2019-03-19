n = int(input())
a = [int(i) for i in input().split()]

y = sum(a) - a[0]
x = a[0]
min_diff = abs(x-y)

for i in range(1,n-1):
    x += a[i]
    y -= a[i]
    diff =  abs(x-y)
    if min_diff > diff:
        min_diff = diff

print(min_diff)

