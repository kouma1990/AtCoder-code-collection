import itertools

N, K = (int(i) for i in input().split())  
heights = [int(input()) for i in range(N)] 

heights.sort()
min_diff = max(heights) - min(heights) 
for i in range(N-K+1):
    diff = heights[i+K-1] - heights[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)
