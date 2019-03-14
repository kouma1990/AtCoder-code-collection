a, b, c = (int(i) for i in input().split())
k = int(input())
print(a+b+c - max([a,b,c]) + max([a,b,c])*(2**k))
