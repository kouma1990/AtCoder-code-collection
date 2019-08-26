import math
n, k = (int(i) for i in input().split())  
a = [int(i) for i in input().split()]

print( 1 + math.ceil((n-k) / (k-1)) )