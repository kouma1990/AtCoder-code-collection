n = int(input())
n = n%30

a = ["1","2","3","4","5","6"]

for i in range(n):
    tmp = a[i%5]
    a[i%5] = a[i%5+1]
    a[i%5+1] = tmp

print("".join(a))