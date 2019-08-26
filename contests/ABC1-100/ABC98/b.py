n = int(input())
s = input()

max_score = 0
for i in range(1,n-1):
    s1 = s[:i]
    s2 = s[i:]
    dic = []

    for x in s1:
        if x in s2 and x not in dic:
            dic.append(x)

    if max_score < len(dic):
        max_score = len(dic)

print(max_score)
