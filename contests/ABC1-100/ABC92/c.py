n = int(input())
a = [int(i) for i in input().split()]

diff = [abs(a[0])]

for i in range(n-1):
    diff.append(abs(a[i+1] - a[i]))

diff.append(abs(a[-1]))

min_cost = 10**10
ori = sum(diff)
a.append(0)
a.insert(0,0)
for i in range(n):
    cost = ori - diff[i] - diff[i+1]
    cost += abs(a[i] - a[i+2])
    print(cost)
