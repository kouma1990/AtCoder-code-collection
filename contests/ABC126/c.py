n,k = (int(i) for i in input().split())

res = 0
for i in range(1,n+1):
    cnt = 0
    now = i
    while True:
        if now >= k:
            break    
        now = now*2
        cnt+=1
    
    res += 1/(n*2**cnt)

print(res)