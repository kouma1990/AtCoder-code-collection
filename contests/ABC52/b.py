n = int(input())
s = input()

res = 0
now = 0
for i in range(n):
    if s[i] == "I":
        now += 1
    else:
        now -= 1

    res = max(res,now)

print(res)