n, k = (int(i) for i in input().split())

if k%2==0:
    a = n // k
    b = n // (k/2) - a
else:
    a = n //k
    b = 0

print( int(a*a*a + b*b*b) )
