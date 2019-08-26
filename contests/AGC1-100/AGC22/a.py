s = input()

dic = "abcdefghijklmnopqrstuvwxyz"

if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)

elif len(s) < 26:
    t = ""
    for x in dic:
        if s.count(x) == 0:
            t = x
            break
    print(s+t)
else:
    for idx,x in enumerate(s):
        t = s[-idx-1]
        l = s[-idx-1:]
        min_s = ""
        for y in l:
            if t < y:
                min_s = y if min_s=="" else min(min_s, y)
        
        if min_s != "":
            break
    print(s[:-idx-1]+min_s)

