import sys
input = sys.stdin.readline
sys.setrecursionlimit(11000)

n = int(input())
ab = [[ (int(i)-1) for i in input().split()] for i in range(n-1)]
c = sorted([int(i) for i in input().split()], reverse=True)

if n==1:
    print(0)
    print(c[0])
    exit()

dic = {}
for i in range(n):
    dic[i] = []

cnt = [0]*n
for a,b in ab:
    dic[a].append(b)
    dic[b].append(a)
    cnt[a] += 1
    cnt[b] += 1

c_idx = 0
res = 0
res_arr = [""]*n
used = [0]*n
def f(idx):
    global c_idx, res, used
    used[idx] = 1
    res_arr[idx] = str(c[c_idx])
    for x in dic[idx]:
        if used[x] == 0:
            c_idx += 1
            res += c[c_idx]
            f(x)

f(cnt.index(1))
print(res)
print(" ".join(res_arr))