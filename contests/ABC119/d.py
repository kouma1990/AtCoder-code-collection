import sys
input = sys.stdin.readline
import bisect

a, b, q = (int(i) for i in input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
x = [int(input()) for i in range(q)]

def get_near(e, x):
    xi = bisect.bisect_left(x,e)
    if xi == 0:
        return [x[0]]
    if xi == len(x):
        return [x[-1]]
    return [x[xi-1], x[xi]]

for e in x:
    s_ = get_near(e,s)
    t_ = get_near(e,t)
    min_dist = 10**11
    for si in s_:
        for ti in t_:
            dist = min(abs(e-si), abs(e-ti)) + abs(si-ti)
            min_dist = min(min_dist, dist)

    print(min_dist)
