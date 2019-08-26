n = int(input())
s = str(n)
f = 0
for i in s:
    f += int(i)

if n % f == 0:
    print("Yes")
else:
    print("No") 