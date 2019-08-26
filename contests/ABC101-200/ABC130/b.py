n, x = (int(i) for i in input().split())
l = [int(i) for i in input().split()]

cnt = 1
now = 0
for y in l:
    now += y
    if now > x:
        break
    cnt += 1

print(cnt)