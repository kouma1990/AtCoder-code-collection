n = int(input())
k = int(input())
x = [int(i) for i in input().split()]

res = 0
c = k/2
for x_ in x:
    if x_ < c:
        res += x_*2
    else:
        res += (k-x_)*2
print(res)