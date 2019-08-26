n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

count = 0
next_a = a[0]
for i in range(n):
    if next_a < b[i]:
        count += next_a + min(a[i+1], b[i]-next_a)
        next_a = max(a[i+1]-b[i]+next_a, 0)
    else:
        count += b[i]
        next_a = a[i+1]

print(count)


