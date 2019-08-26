n, k = (int(i) for i in input().split())
x = [int(i) for i in input().split()]

min_dist = 10**10
for i in range(n-k+1):
    if x[i] > 0:
        dist = x[i+k-1]
    elif x[i+k-1] < 0:
        dist = -x[i]
    else:
        dist = x[i+k-1] - x[i] + min(-x[i], x[i+k-1])

    if dist < min_dist:
        min_dist = dist

print(min_dist)