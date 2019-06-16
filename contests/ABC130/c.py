W,H,x,y = (int(i) for i in input().split())

is_double = 0
if x == W/2 and y == H/2:
    is_double = 1

print("{} {}".format(H*W/2,is_double))