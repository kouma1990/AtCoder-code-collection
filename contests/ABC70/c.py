n = int(input())
a = [int(input()) for i in range(n)]

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
# 最小公倍数lcm
def lcm(a, b):
    return (a*b) // gcd(a,b)

# リストに対してgcd, lcm求める
import functools
result_lcm = functools.reduce(lcm, a)

print(result_lcm)