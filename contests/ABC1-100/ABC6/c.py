n, m = (int(i) for i in input().split()) 
if m < n*2 or n*4 < m:
    print("-1 -1 -1")

else:
    b_ = min(n, m-2*n)
    c = max(0, m-3*n)
    b = b_ - c
    a = n - b - c
    print("{} {} {}".format(a,b,c))