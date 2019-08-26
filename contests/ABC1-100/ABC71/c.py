n = int(input())
a = sorted([int(i) for i in input().split()], reverse=True)

x = []
for i in range(n-1):
    if a[i] == a[i+1]:
        a[i+1] = -1
        x.append(a[i])
        if len(x) == 2:
            break

if len(x) == 2:
    print(x[0]*x[1])
else:
    print(0)
