n = int(input())
k = int(input())

result = 1
for i in range(n):
    if result < k:
        result *= 2
    else:
        result += k

print(result)