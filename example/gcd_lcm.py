# 最大公約数gcd, 
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

# 最小公倍数lcm
def lcm(a, b):
    return (a*b) // gcd(a,b)

# リストに対してgcd, lcm求める
import functools
a = [3, 6, 9, 12]
result_gcd = functools.reduce(gcd, a)
result_lcm = functools.reduce(lcm, a)

print(result_gcd)
print(result_lcm)

