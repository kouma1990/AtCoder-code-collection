n,x = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
bins = ("0"*20 + bin(x)[2:])[-n:][::-1]

res = 0
for i,a_ in enumerate(a):
    res+= a_*int(bins[i])

print(res)