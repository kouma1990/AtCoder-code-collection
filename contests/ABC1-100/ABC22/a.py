n,s,t = (int(i) for i in input().split())
w = int(input())
a = [int(input()) for i in range(n-1)]

cnt = 0
if s<=w and w<=t:
    cnt+=1
for x in a:
    w = w+x
    if s<=w and w<=t:
        cnt+=1


print(cnt)