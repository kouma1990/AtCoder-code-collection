a, b, c = (int(i) for i in input().split())

res = a+b
res = a+c if a+c < res else res
res = b+c if b+c < res else res

print(res)