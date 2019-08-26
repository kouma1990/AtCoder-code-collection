n = int(input())
a = [int(input()) for i in range(3)]

if n in a:
    print("NO")
    exit()
    
for i in range(100):
    flg = True
    for t in [3,2,1]:
        if n - t not in a:
            n = n-t
            flg = False
            break

    if flg:
        break

    if n <= 0:
        print("YES")
        exit()

print("NO")