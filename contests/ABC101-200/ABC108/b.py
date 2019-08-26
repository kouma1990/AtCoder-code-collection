a, b, c, d = (int(i) for i in input().split())
x = c - a
y = d - b
print("{} {} {} {}".format(c-y, d+x, a-y, b+x))