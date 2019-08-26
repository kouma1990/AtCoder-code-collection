import sys
input = sys.stdin.readline
r,c,k = (int(i) for i in input().split())
n = int(input())
rc = [[int(i)-1 for i in input().split()] for i in range(n)]

arr = [[0 for i in range(c)] for j in range(r)]
cntr = [0]*r
cntc = [0]*c

for j,i in rc:
    arr[j][i] = 1
    cntr[j] += 1
    cntc[i] += 1

cnt = 0
for j in range(r):
    for i in range(c):
        if cntr[j]+cntc[i]-arr[j][i] == k:
            cnt+=1

print(cnt)