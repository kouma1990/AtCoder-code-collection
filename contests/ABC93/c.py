a = sorted([int(i) for i in input().split()])

count = (a[1]-a[0])//2
a[0] += 2*count

if a[0] != a[1]:
    a[0] += 1
    a[2] += 1
    count += 1

count += a[2]-a[0]
print(count)
