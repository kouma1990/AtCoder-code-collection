n = int(input())
a = [int(input()) for i in range(n)]

from collections import Counter
c = Counter(a)

print(sum(c.values()) - len(c.values()))