k, s = (int(i) for i in input().split())

cnt = 0
for x in range(k+1):
    c = s-x
    cnt += max(min(k,c)-max(0,c-k)+1,0)

print(cnt)