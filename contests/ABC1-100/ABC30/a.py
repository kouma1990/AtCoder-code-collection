a, b, c, d = (int(i) for i in input().split())

if b/a > d/c:
    print("TAKAHASHI")
elif b/a < d/c:
    print("AOKI")
else:
    print("DRAW")