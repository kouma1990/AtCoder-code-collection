n, k = (int(i) for i in input().split())

res = 0 if n % k == 0 else 1
print(res)