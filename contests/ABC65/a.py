x,a,b = (int(i) for i in input().split())

if b-a <= 0:
    print("delicious")
elif b-a <= x:
    print("safe")
else:
    print("dangerous")