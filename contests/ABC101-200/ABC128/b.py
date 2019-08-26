n = int(input())
sp = [[i for i in input().split()] for i in range(n)]

dic = {}
for x,p in sp:
    if x in dic:
        dic[x].append(int(p))
    else:
        dic[x] = [int(p)]

res_l = []
for x,p in sp:
    res = 0
    flg = False
    for k in sorted(dic):
        if x != k:
            res+=len(dic[k])
        else:
            l = sorted(dic[k], reverse=True)
            #print(l)
            for i in l:
                res += 1
                if int(i) == int(p):
                    flg == True
                    res_l.append(res)
                    break

        if flg:
            break

xx = [0]*n
for i,x in enumerate(res_l):
    xx[x-1] = i+1

for x in xx:
    print(x)