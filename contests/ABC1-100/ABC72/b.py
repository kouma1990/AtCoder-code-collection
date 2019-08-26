s = input()

res = ""
for i in range(len(s)):
    if i%2==0:
        res+=s[i]

print(res)