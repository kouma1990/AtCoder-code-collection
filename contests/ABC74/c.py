a, b, c, d, e, f = (int(i) for i in input().split())

used = [[-1 for i in range(3000)] for j in range(3000)]
def dfs(w,s,wa,sa):
   
    if w+s > f or e*w/100 < s:
        w -= wa
        s -= sa
        if w==0:
            return [0,0,s]
        else:
            return [100*s/(w+s), w, s]

    if used[w][s] == 1:
        return [0,0,0]
    d1 = dfs(w+100*a,s,100*a,0)
    d2 = dfs(w+100*b,s,100*b,0)
    d3 = dfs(w,s+c,0,c)
    d4 = dfs(w,s+d,0,d)
    
    dl = [d1,d2,d3,d4]
    max_n = max([d1[0], d2[0], d3[0], d4[0]])
    for x in dl:
        if x[0] == max_n:
            used[w][s] = 1
            return x

res = dfs(0,0,0,0)

print("{} {}".format(res[1]+res[2], res[2]))