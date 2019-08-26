n,m,k = (int(i) for i in input().split())

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

x = combinations_count((n*m-2), k-2)

