X = input()
l = len(X)

result = 1000
for i in range(l-2):
    num = abs(int(X[i:i+3]) - 753)
    if num < result:
        result = num

print(result)