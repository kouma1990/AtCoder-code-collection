a, b = (int(i) for i in input().split())

count = 0
for i in range(a, b+1):
    flg = True
    s = str(i)
    for j in range(len(s)):
        if s[j] != s[-(j+1)]:
            flg = False
            break

    if flg:
        count+=1

print(count)