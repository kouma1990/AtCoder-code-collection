x,y,z,k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

ab = []
for a_ in a:
    for b_ in b:
        ab.append(a_+b_)

res = []
for ab_ in sorted(ab, reverse=True)[:k]:
    for c_ in sorted(c, reverse=True)[:k]:
        res.append(ab_+c_)

for x in sorted(res, reverse=True)[:k]:
    print(x)