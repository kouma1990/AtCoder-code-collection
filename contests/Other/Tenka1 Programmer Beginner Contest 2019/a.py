a, b, c = (int(i) for i in input().split())


if (a<c and c<b) or (b<c and c<a):
    print("Yes")
else:
    print("No")