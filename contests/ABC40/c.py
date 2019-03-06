n = int(input()) 
a = [int(input()) for i in range(n)] 

dp = [0, abs(a[1]-a[0])]
for i in range(2, n):
    x1 = dp[i-2] + abs(a[i]-a[i-2])
    x2 = dp[i-1] + abs(a[i]-a[i-1])
    dp.append(min(x1, x2))

print(dp[-1])