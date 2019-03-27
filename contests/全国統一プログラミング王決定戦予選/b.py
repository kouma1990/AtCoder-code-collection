from collections import Counter
n = int(input())
a = input()
b = input()
c = input()

count = 0
for i in range(n):
    co = Counter([a[i], b[i], c[i]])
    count += 3-max(co.values())

print(count)