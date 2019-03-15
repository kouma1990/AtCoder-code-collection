import math
n = int(input())
e = [[int(i) for i in input().split()] for i in range(n-1)]

result = []
for i in range(n-1):
    t = e[i][0] + e[i][1]
    for x in e[i+1:]:
        if t <= x[1]:
            t = x[0] + x[1]
            continue
        t = math.ceil((t-x[1])/x[2])*x[2] + x[1] + x[0]
    result .append(t)

result.append(0)
for x in result:
    print(x)

"""
if n==1:
    print(0)
    exit()

result = [0, e[-1][0]+e[-1][1]]
if n==2:
    for x in result[::-1]:
        print(x)
    exit()

if n > 2:
    for i in range(1,n-1):
        a = e[-i-1][0] + e[-i-1][1]
        if a <= e[-i][1]:
            result.append(result[-1]) 
            continue
        b = math.ceil((a - e[-i][1]) / e[-i][2])
        result.append(result[-1]+b* e[-i][2])
        #print(e[-i])

for x in result[::-1]:
    print(x)
"""