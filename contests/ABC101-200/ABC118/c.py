import functools
n = int(input())
m = [int(i) for i in input().split()]  
 
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
  
gcd = functools.reduce(gcd, m)
print(gcd)