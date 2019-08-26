w,h = (int(i) for i in input().split())

if (h//3)*4 == w:
    print("4:3")
else:
    print("16:9")