n = int(input())
h = [int(i) for i in input().split()]

count = 0
while True:
    flg_s = False
    for i in range(n):
        if flg_s and h[i] == 0:
            break
        if h[i] > 0:
            flg_s = True
            h[i] -= 1

    if not flg_s:
        break
    count += 1

print(count)