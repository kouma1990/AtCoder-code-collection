k,a,b = (int(i) for i in input().split())

n = 1
if b-a < 3 or k < a+1:
    print(n+k)
    exit()

k -= a-1
n += a-1

n += (k//2)*(b-a) + k%2
print(n)