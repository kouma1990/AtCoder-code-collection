h, w = (int(i) for i in input().split())
e = [input() for i in range(h)]

flg = True
for j in range(h):
    for i in range(w):
        if e[j][i] == ".":
            continue
        if i != 0 and e[j][i-1] == "#":
            continue
        if j != 0 and e[j-1][i] == "#":
            continue
        if i != w-1 and e[j][i+1] == "#":
            continue
        if j != h-1 and e[j+1][i] == "#":
            continue
        flg = False
        break

    if not flg:
        break

if flg:
    print("Yes")
else:
    print("No")