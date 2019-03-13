n = int(input())
a = [int(i) for i in input().split()]

b = []

for i in range(n):
    b.append(a[i]-(i+1))

b = sorted(b)

x = b[n//2] if n%2==1 else (b[n//2] + b[(n//2)-1]) // 2

sum_num = 0
for b_ in b:
    sum_num += abs(b_-x)

print(sum_num)