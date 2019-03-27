a, b, x = (int(i) for i in input().split())

res = (b//x-a//x) + (1 if a%x==0 else 0)

print(res)