n = int(input())
a = [int(input()) for i in range(n)]

dp = [{0:1}]

sum_num = sum(a)

for x in a:
    dp.append({})
    for k, v in dp[-2].items():
        if k in dp[-1]:
            dp[-1][k] += v
        else:
            dp[-1][k] = v

        if k+x in dp[-1]:
            dp[-1][k+x] += v
        else:
            dp[-1][k+x] = v

print(dp[-1])

