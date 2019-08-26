a, b, c = (int(i) for i in input().split())
 
result = b / a
result = int(min(result, c))
print(result)