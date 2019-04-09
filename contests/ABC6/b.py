n = int(input())

if n < 3:
    print(0)
    exit()
a=[0,0,1]

res = 1
for i in range(n-4):
    a[i%3] = sum(a)%10007

print(sum(a)%10007)