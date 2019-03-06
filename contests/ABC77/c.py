import bisect
n = int(input()) 
A = sorted([int(i) for i in input().split()] )
B = sorted([int(i) for i in input().split()] )
C = sorted([int(i) for i in input().split()] )

b_count = []
pre_b = 0
for b in B:
    current_count = bisect.bisect_left(A,b)
    b_count.append(pre_b + current_count)
    pre_b += current_count

result = 0
for c in C:
    index = bisect.bisect_left(B,c)
    if index == 0:
        continue
    result += b_count[index-1]
print(result)