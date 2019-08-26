n, x = (int(i) for i in input().split()) 
a = sorted(list(set([int(i) for i in input().split()])))

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

import functools

if len(a) == 1:
    print(abs(a[0] - x))
    exit()

diff = []
for i in range(len(a)-1):
    diff.append(a[i+1] - a[i])

list_gcd = functools.reduce(gcd, diff)

import bisect

bi_index = bisect.bisect_left(a, x)
if bi_index == len(a):
    print(gcd(list_gcd, x-a[-1]))
    exit()

if a[bi_index] == x:
    print(list_gcd)
    exit()

if bi_index == 0:
    print(gcd(list_gcd, a[0]-x))
    exit()

print(functools.reduce(gcd, [list_gcd, x-a[bi_index-1], a[bi_index]-x ]))
