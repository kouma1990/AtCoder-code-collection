a = [int(input()) for i in range(5)]

m = 0
res = 0
for x in a:
    if x%10 != 0:
        t = 10 - x%10
    else:
        t = 0
    res += x+t

    m = max(m,t)

print(res-m)