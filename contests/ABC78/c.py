n,m = (int(i) for i in input().split())

result = ((n-m)*100 + m*1900)*2**m
print(result)