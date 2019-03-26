W, a, b = (int(i) for i in input().split())

if a<b:
    print( max(b-W-a, 0))
else:
    print( max(a-W-b, 0))