n = int(input())
a, b = (int(i) for i in input().split())
p = [int(i) for i in input().split()]

x0 = list(filter(lambda x:x<=a, p))
x1 = list(filter(lambda x:a<x and x<=b, p))
x2 = list(filter(lambda x:b<x, p))

print(min([len(x0), len(x1), len(x2)]))