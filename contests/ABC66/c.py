n = int(input())
a = [int(i) for i in input().split()]

x = a[::2]
y = a[1::2]

if n%2==0:
    res = y[::-1] + x
else:
    res = x[::-1] + y

res = list(map(str, res))
print(' '.join(res))
