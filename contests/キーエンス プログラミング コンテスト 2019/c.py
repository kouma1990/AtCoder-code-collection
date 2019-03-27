#WA
import copy
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

inf = 10**10

def f(idx, cnt, arr):
    if idx == n:
        return cnt

    flg = True
    res = []
    for i, x in enumerate(arr):
        if x >= b[idx]:
            flg=False
            l = copy.copy(arr)
            l.pop(i)
            res.append(f(idx+1, cnt+(0 if x==a[idx] else 1), l))

    if flg:
        return inf

    return min(res)

res = f(0,0,a)

print(res)
