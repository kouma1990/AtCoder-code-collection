n,a,b = (int(i) for i in input().split())

print("{} {}".format(min(a,b), max(a+b-n,0) ))