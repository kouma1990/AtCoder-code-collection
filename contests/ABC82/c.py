n = int(input())
a = [int(i) for i in input().split()]


count = len([i for i in a if i > 10**5])
a = [e for e in a if e <= 10**5]
dic = list(set(a))
for x in dic:
    if a.count(x) > x:
        count+= a.count(x) - x
    elif a.count(x) < x:
        count += a.count(x)
print(count)