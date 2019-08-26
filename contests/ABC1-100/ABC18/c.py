r,c,k = (int(i) for i in input().split())
s = [input() for i in range(r)]

cnt = 0
skip = 0
for y in range(k-1,r-k+1):
    for x in range(k-1,c-k+1):
        flg=True
        for j in range(-k+1,k):
            for i in range(-k+1+abs(j),k-abs(j)):
                dy = y+j
                dx = x+i
                if s[dy][dx]=="x":
                    flg = False
                    break
            if not flg:
                break

        if flg:
            cnt += 1

print(cnt)