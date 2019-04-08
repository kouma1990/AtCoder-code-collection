n,t = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

now = 0
for x in a:
    for i in range(10**10):
        if x+t*i >= now:
            now = x+t*i
            break

print(now)