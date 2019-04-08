import math
n = int(input())
a = [int(i) for i in input().split()]

a = list(filter(lambda x:x>0, a))
print(math.ceil(sum(a)/len(a)))