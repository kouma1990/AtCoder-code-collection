a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

flg = False
for x in a:
    for y in b:
        if x==y:
            flg = True

if flg:
    print("YES")
else:
    print("NO")