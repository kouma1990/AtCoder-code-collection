import sys
input = sys.stdin.readline
n,q = (int(i) for i in input().split())
s = input()
td = [[i for i in input().split()] for i in range(q)][::-1]

now = s[0]
pre = ""
idx = 0
for t,d in td:
    if t==now and d=="L":
        idx += 1
        now = s[idx]
        pre = s[idx-1]
    elif t==pre and d=="R" and idx != 0:
        idx -= 1
        now = s[idx]
        pre = s[max(0,idx-1)]
        
res = n-idx
now = s[n-1]
pre = ""
idx = n-1
for t,d in td:
    if t==now and d=="R":
        idx -= 1
        now = s[idx]
        pre = s[idx+1]
    elif t==pre and d=="L" and idx != n-1:
        idx += 1
        now = s[idx]
        pre = s[min(n-1,idx+1)]

print(max(0,res-(n-1-idx)))
