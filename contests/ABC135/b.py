n = int(input())
p = [int(i) for i in input().split()]

sorted_p = sorted(p)

count = 0
for i in range(n):
    if p[i] != sorted_p[i]:
        count += 1

if count > 2:
    print("NO")
else:
    print("YES")