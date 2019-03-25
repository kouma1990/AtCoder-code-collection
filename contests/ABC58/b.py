o = input()
e = input()

res = ""
for i in range(len(o)):
    res += o[i]
    if i < len(e):
        res += e[i]

print(res)