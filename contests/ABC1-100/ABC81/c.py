n, k = (int(i) for i in input().split())
a = [int(i)-1 for i in input().split()]

import collections
c = collections.Counter(a)
values, counts = zip(*c.most_common(k))
print(n-sum(counts))
