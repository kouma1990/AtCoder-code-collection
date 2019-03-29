s = input()

res = ""
for x in s:
    if x =="B":
        res = res[:-1]
    else:
        res += x

print(res)