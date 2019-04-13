n = int(input())
h = [int(i) for i in input().split()]

cnt = 0
m = 0
for x in h:
    if m <= x:
        cnt+=1
        m=x

print(cnt)