a, b = (int(i) for i in input().split())

if abs(a-b) % 2 == 1:
    print("IMPOSSIBLE")
    exit()

diff = abs(a-b)
diff_2 = diff // 2

print(max(a,b) - diff_2)