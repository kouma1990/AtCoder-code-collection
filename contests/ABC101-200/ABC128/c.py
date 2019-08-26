n,m = (int(i) for i in input().split())
ks = e = [[int(i) for i in input().split()] for i in range(m)]
p = [int(i) for i in input().split()]

on = []
for x in ks:
    o = 0
    for s in x[1:]:
        o += 2**(s-1)
    on.append(o)

res = 0
for x in range(2**n):
    flg = True
    for i,o in enumerate(on):
        if p[i] != bin(o&x).count("1") % 2:
            flg = False
            break

    if flg:
        res += 1
       
print(res)