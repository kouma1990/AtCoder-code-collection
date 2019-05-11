r,g,b,n = (int(i) for i in input().split())

cnt = 0
for i in range((n+1)//r + 1):
    for j in range((n+1)//g + 1):
        s = i*r + g*j
        if s>n:
            continue
        if (n-s)%b == 0:
            cnt += 1


print(cnt)