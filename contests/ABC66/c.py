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
#print(x)
#print(y)

exit()
flg = True
if n % 2 == 0:
    flg = False

b = []

for x in a:
    if flg:
        b.insert(0, str(x))
    else:
        b.append(str(x))

    flg = not flg

print(' '.join(b))