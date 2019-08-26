n = int(input())

min_len = len(str(n))
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        l = max(len(str(i)), len(str(n//i)))
        min_len = min(min_len, l)


print(min_len)