s = input()


pre = "R"
r_cnt = 1
l_cnt = 0
res = []
for idx_,x in enumerate(s[1:]):
    idx = idx_+1
    if pre == "R":
        if pre != x:
            pre = "L"
        else:
            r_cnt += 1
            res.append(str(0))
    if pre == "L":
        if pre != x:
            # 集計
            res.append( str((r_cnt+1)//2 + l_cnt//2) )
            res.append( str(r_cnt//2 + (l_cnt+1)//2) )
            for i in range(l_cnt-1):
                res.append(str(0))
            pre = "R"
            r_cnt = 1
            l_cnt = 0
        else:
            l_cnt += 1

        if idx == len(s)-1:
            res.append( str((r_cnt+1)//2 + l_cnt//2) )
            res.append( str(r_cnt//2 + (l_cnt+1)//2) )
            for i in range(l_cnt-1):
                res.append(str(0))

print(" ".join(res))