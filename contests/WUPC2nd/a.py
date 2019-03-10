n, m = (int(i) for i in input().split())  

result = sum(map(lambda x:x**2, list(range(n+1)))) % m
print(result)