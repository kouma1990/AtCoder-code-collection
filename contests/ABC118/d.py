n, m = (int(i) for i in input().split())
a = sorted([int(i) for i in input().split()])

dic = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
cost = []
b = {}
for x in a:
    cost.append(dic[x])
    b[dic[x]] = x

cost = sorted(list(set(cost)))

dp = [0]*(n+1)
for x in cost:
    dp[x] = [b[x]]


for i in range(cost[0]*2, n+1):
    for x in cost:
        if i - x > 0 and dp[i-x] != 0:
            dp[i] = dp[i-x] + [b[x]]
            break

print("".join(list(map(str,sorted(dp[-1], reverse=True)))))
