n = int(input())

a = [2,1]
for i in range(2,n+1):
    a.append(a[-1]+a[-2])

print(a[-1])