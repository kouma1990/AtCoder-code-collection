n = int(input())

if n==1:
    print(0)
    exit()
    
s = 0
for i in range(1, int(n**(1/2)+1) ):
    ans = (n-i) // i
    if n//ans == n%ans:
        s+=ans
print(s)