s = input()

res = 0
W_cnt = 0
for x in s[::-1]:
    if x == "W":
        W_cnt += 1
    else:
        res += W_cnt
print(res)