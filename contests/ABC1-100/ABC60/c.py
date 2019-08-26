n,t = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

time = t
for i in range(1,n):
    if a[i]-a[i-1] < t:
        time += a[i]-a[i-1]
    else:
        time += t
print(time)