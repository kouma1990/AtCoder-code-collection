N = int(input())
T, A = (int(i) for i in input().split()) 
h_list = [int(i) for i in input().split()]

min_diff = 10000
index = 1
min_index = 0
for h in h_list:
    t = T-h*0.006
    diff = abs(t-A)
    if min_diff > diff:
        min_diff = diff
        min_index = index

    index += 1

print(min_index)