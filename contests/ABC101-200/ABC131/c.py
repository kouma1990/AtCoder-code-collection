import math
# 最大公約数gcd, 
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

# 最小公倍数lcm
def lcm(a, b):
    return (a*b) // gcd(a,b)

a, b, c, d = (int(i) for i in input().split())

cd = lcm(c,d)
r = b-a+1

# 丸め誤差を考慮
min_c = a//c + (1 if a%c!=0 else 0)
max_c = b//c
min_d = a//d + (1 if a%d!=0 else 0)
max_d = b//d
min_cd = a//cd + (1 if a%cd!=0 else 0)
max_cd = b//cd

c_num = max_c-min_c+1
d_num = max_d-min_d+1
cd_num = max_cd-min_cd+1

print(r-c_num-d_num+cd_num)
