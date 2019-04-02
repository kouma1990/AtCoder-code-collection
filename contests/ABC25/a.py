s = sorted(input())
n = int(input())

l = []
for i in s:
    for j in s:
        l.append(i+j)

print(l[n-1])

