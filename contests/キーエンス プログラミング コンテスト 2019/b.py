s = input()

d = len(s)-7
for i in range(len(s)-d+1):
    ns = ""
    for j in range(len(s)):
        if j >= i and j < i+d:
            continue
        ns += s[j]

    if ns == "keyence":
        print("YES")
        exit()
print("NO")