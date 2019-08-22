n = int(input())
h = [int(i) for i in input().split()]

flg = True
for i in range(n-1):
    if h[n-1-i] + 1 < h[n-2-i]:
        flg = False
        break
    
    if h[n-1-i] < h[n-2-i]:
        h[n-2-i] -= 1

if flg:
    print("Yes")
else:
    print("No")
