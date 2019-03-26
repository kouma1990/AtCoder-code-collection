import collections

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

x = a+b+c
c = collections.Counter(x)

if len(list(filter(lambda x:x>2,c.values()))) > 0:
    print("NO")
else:
    print("YES")
