s = [input() for i in range(12)]

cnt = 0
for x in s:
    if x.count("r") > 0:
        cnt += 1

print(cnt)