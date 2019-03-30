a = [int(i) for i in input().split()]

if a.count(a[0]) == 3:
    print("Yes")
else:
    print("No")