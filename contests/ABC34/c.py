import math
w,h = (int(i)-1 for i in input().split())

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(combinations_count(w+h,w)%(10**9+7))