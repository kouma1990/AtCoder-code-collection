n = int(input())
ab = sorted([[int(i) for i in input().split()] for i in range(n)], key=lambda x:x[1])[::-1]

time = ab[0][1] - ab[0][0]
for a,b in ab[1:]:
    time = min(time, b)
    time -= a

print("No" if time < 0 else "Yes")