x,y,z = (int(i) for i in input().split())

if x < y+2*z:
    print(0)
    exit()

x -= z
result = x//(y+z)
print(result)