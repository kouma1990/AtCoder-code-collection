x = int(input())
res = (x // 11)*2
if x%11 == 0:
    pass
elif x%11 < 7:
    res += 1
else:
    res += 2
print(res)