n = int(input())

res = 1
for i in range(10):
    if 2**i > n:
        res = 2**(i-1)
        break

print(res)
