n = int(input())
s = input()

def check(x):
    if x == ".":
        return 0
    else:
        return 1

if n < 4:
    print(0)
else:
    dp = [0]*n
    dp[0] = 0
    dp[1] = check(s[1])
    dp[2] = check(s[2])

    for i in range(3,n):
        ch = check(s[i])
        dp[i] = min([dp[i-3]+ch, dp[i-2]+ch, dp[i-1]+ch])

    print(dp[-1])