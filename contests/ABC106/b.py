n = int(input())

if n <= 104:
    print(0)
    exit()


count = 1
for i in range(106, n+1):
    if i % 2 == 0:
        continue
    arr = []
    for j in range(1,i+1):
        if i % j == 0:
            arr.append(j)
    if len(arr) == 8:
        count+=1

print(count)
    