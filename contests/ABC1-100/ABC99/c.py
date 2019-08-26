n = int(input())

pre_list=[1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 46656, 59049]
dp = [-1]*(n+1)
dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
    a = []
    a.append(dp[i-1]+1)
    for j in pre_list:
        if i-j >= 0:
            a.append(dp[i-j]+1)
        else:
            break

    dp[i] = min(a)

print(dp[-1])
