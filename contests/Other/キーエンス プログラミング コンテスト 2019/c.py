n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
diff = [0]*n

neg = 0
cnt = 0
for i in range(n):
    x = a[i]-b[i]
    diff[i] = x
    if x < 0:
        cnt += 1
        neg += x

if sum(diff)<0:
    print(-1)
    exit()

for x in sorted(diff, reverse=True):
    if neg >= 0:
        break
    cnt += 1
    neg += x

print(cnt)
