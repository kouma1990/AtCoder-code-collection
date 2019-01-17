import itertools

N, K = (int(i) for i in input().split())  
heights = [int(input()) for i in range(N)] 
heights_lists = list(itertools.combinations(heights, K))

min_diff = max(heights) - min(heights) 
for heights_one in heights_lists:
    if min_diff > (max(heights_one) - min(heights_one) ):
        min_diff = (max(heights_one) - min(heights_one) )

print(min_diff)
