n = int(input())
s = [input() for i in range(n)]

res = ""
for i in range(len(s[0])):
    l = len(s[0]) - i
    for j in range(len(s[0])):
        if j+l > len(s[0]):
            break

        cs = s[0][j:j+l]
        print(cs)
        flg = True
        for x in s[1:]:
            if x.count(cs) == 0:
                flg = False
                break

        if flg:
            if res == "":
                res = cs
            else:
                res = min(res,cs)
        
    if res != "":
        break

print(res)