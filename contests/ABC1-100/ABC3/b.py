s = input()
t = input()

dic = "atcoder"
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    if (s[i]=="@" and t[i] in dic) or (s[i] in dic and t[i]=="@"):
        continue
    else:
        print("You will lose")
        exit()

print("You can win")
