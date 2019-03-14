n = int(input())

s = 0
for i in str(n):
    s += int(i)

print("Yes" if n%s==0 else "No")