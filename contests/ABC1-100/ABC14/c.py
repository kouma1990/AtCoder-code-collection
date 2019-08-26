import sys
input = sys.stdin.readline
q = int(input())
lr = [[int(i) for i in input().split()] for i in range(q)]
n = 1000001
cnt = [0]*n

for l,r in lr:
    cnt[l] +=1
    if r<n-1:
        cnt[r+1] -=1
        
res = 0
c = 0
for i,x in enumerate(cnt):
    c += x
    res = max(res,c)


print(res)
