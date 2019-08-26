n,m = (int(i) for i in input().split())
a = [input() for i in range(n)]
b = [input() for i in range(m)]

for i in range(n-m+1):
    for j in range(n-m+1):
        flg = True
        for y in range(m):
            for x in range(m):
                if a[i+y][j+x] != b[y][x]:
                    flg = False
                    break
            if flg == False:
                break

        if flg:
            print("Yes")
            exit()

print("No")