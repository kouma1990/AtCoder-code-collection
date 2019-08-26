n = int(input())
a = [input() for i in range(n)]

import collections
c = collections.Counter(a)

print(c.most_common()[0][0])