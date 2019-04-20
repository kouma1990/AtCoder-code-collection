n = int(input())
s = input()
k = int(input())

a= s[k-1]

res = ""
for idx,x in enumerate(s):
    if s[idx] != a:
        res += "*"
    else:
        res += x
print(res)