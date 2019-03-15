n, a, b = (int(i) for i in input().split())

l = []
for i in range(n+1):
    s = str(i)
    sum_ = 0
    for x in s:
        sum_ += int(x)
    
    if a <= sum_ and sum_ <= b:
        l.append(i)

print(sum(l))