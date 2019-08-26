s = input()

cnt = 0
now = s[0]

for x in s:
    if x != now:
        now = x
        cnt += 1

print(cnt)