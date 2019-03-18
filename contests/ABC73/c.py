import collections
n = int(input())
a = [int(input()) for i in range(n)]

c = collections.Counter(a)
c_odd = list(filter(lambda x:x%2==1,c.values()))

print(len(c_odd))