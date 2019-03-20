h,w = (int(i) for i in input().split())
a = [input() for i in range(h)]

x = "#"*(w+2)
print(x)
for b in a:
    print("#"+b+"#")
print(x)