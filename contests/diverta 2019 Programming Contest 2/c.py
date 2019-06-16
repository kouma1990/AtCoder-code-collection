n = int(input())
a = sorted([int(i) for i in input().split()])

if n == 2:
    print(a[1] - a[0])
    print("{} {}".format(a[1], a[0]))
    exit()

if a[0] <= 0 and 0 <= a[-1]:
    import bisect
    print(sum(map(lambda x: abs(x), a)))
    x0 = bisect.bisect_left(a,0)

    # 0以下から0以上をひいていく（一番大きいものを除く）
    if a[-2] >= 0:
        if x0 == 0:
            x0 += 1
        print("{} {}".format(a[0], a[x0]))
        res = a[0] - a[x0]

        for x in a[x0+1:-1]:
            print("{} {}".format(res, x))
            res -= x
    else:
        res = a[0]

    # 一番大きいものから上のものと負の数を引いていく
    print("{} {}".format(a[-1], res))
    res = a[-1] - res
    for x in a[1:x0]:
        print("{} {}".format(res,x))
        res -= x

elif a[0] > 0:
    print(sum(a) - 2*a[0])

    print("{} {}".format(a[0],a[1]))
    res = a[0] - a[1]
    for x in a[2:-1]:
        print("{} {}".format(res, x))
        res -= x
    
    print("{} {}".format(a[-1], res))
else:
    print(-sum(a) + 2*a[-1])

    print("{} {}".format(a[-1],a[-2]))
    res = a[-1] - a[-2]
    for x in a[:-2]:
        print("{} {}".format(res, x))
        res -= x
    