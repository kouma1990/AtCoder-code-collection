n, x = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

cnt = 0
for a_ in sorted(a):
    if x >= a_:
        x -= a_
        cnt += 1 
    else:
        x = 0
        break

if x > 0:
    cnt -= 1
print(cnt)