n,k=(int(i) for i in input().split())
t=[[int(i) for i in input().split()] for i in range(n)]

def f(qi, mem):
    if qi == n:
        return mem

    l = []
    for i in range(k):
        l.append(f(qi+1, mem^t[qi][i]))

    return min(l)

if f(0,0) == 0:
    print("Found")
else:
    print("Nothing")