n = int(input().replace(" ", ""))

result = "No"
for i in range(n):
    t = i**2
    if t == n:
        result = "Yes"
        break

    if t > n:
        break

print(result)