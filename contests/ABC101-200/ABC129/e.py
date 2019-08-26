l = input()

def countValues(n): 
    cnt  =1
    while n:
        if n&1==0:
            cnt += 1
        n = n>>1

    return 1<<cnt
# Driver Code 
n = int(l,2)
print(n)
print(countValues(n)%1000000007); 

print(countValues(n))