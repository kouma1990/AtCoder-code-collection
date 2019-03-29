a = [int(i) for i in input().split()]

if a.count(5) == 2 and a.count(7) == 1:
    print("YES")
else:
    print("NO")