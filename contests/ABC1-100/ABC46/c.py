n = int(input())
ta = [[int(i) for i in input().split()] for i in range(n)]

ct = ta[0][0]
ca = ta[0][1]

for i in range(1, n):
    t, a = ta[i]

    if ct / t > ca / a:
        if ct%t == 0:
            rate = ct//t
        else:
            rate = ct//t+1
    else:
        if ca%a == 0:
            rate = ca//a
        else:
            rate = ca//a+1
    ct = rate * t
    ca = rate * a
print(ct+ca)