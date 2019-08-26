l, h = (int(i) for i in input().split())
n = int(input())
a = [int(input()) for i in range(n)]

for x in a:
    if x < l:
        print(l-x)
    elif h < x:
        print(-1)
    else:
        print(0)