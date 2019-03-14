n = int(input())
d, x = (int(i) for i in input().split())
a = [int(input()) for i in range(n)]

count = n
for i in a:
    count += (d-1) // i

print(count + x)