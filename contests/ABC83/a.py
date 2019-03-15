a, b, c, d = (int(i) for i in input().split())
x=a+b
y=c+d
if x > y:
    print("Left")
if x < y:
    print("Right")
if x == y:
    print("Balanced")
