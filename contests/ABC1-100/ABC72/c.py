import collections
n = int(input())
a = [int(i) for i in input().split()]

c = collections.Counter(a)
res = 0
for i in range(10**5):
    num = c[i-1] + c[i] + c[i+1]
    if res < num:
        res = num
print(res)