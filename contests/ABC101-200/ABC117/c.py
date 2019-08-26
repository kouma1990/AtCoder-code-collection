n, m = (int(i) for i in input().split())  
x = sorted([int(i) for i in input().split()])

if m > 1:
    x_diff = []
    for i in range(m-1):
        x_diff.append(x[i+1] - x[i])
else:
    x_diff = [0]

if n > 1:
    x_diff = sorted(x_diff)[:-(n-1)]

print(sum(x_diff))