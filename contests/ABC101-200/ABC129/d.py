h,w = (int(i) for i in input().split())
s = [input() for i in range(h)]

wl = [0]*h*w
hl = [0]*h*w
for j in range(h):
    for i in range(w):
        if s[j][i] == "#":
            continue

        # 横方向
        if i != 0 and wl[w*j+i-1] != 0:
            wl[w*j+i] = wl[w*j+i-1]
        else:
            if "#" in s[j][i:]:
                wl[w*j+i] = s[j][i:].index("#")
            else:
                wl[w*j+i] = w-i

        # 縦方向
        if j != 0 and hl[w*(j-1)+i] != 0:
            hl[w*j+i] = hl[w*(j-1)+i]
        else:
            for y in range(j,h):
                if s[y][i] == "#":
                    break
                hl[w*j+i] = y-j+1
            

res = [x + y for (x, y) in zip(wl, hl)]

print(max(res)-1)