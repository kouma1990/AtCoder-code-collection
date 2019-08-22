n = int(input())

cnt = 0
for i in range(n):
    s = str(i+1)
    if len(s)%2==1:
        cnt+=1

print(cnt)