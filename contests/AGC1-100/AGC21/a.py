n = input()

res = 0


if n[0] != "9":
    if len(n[1:]) == n.count("9"):
        res = int(n[0]) + 9*n.count("9")
    else:
        res = int(n[0])-1 + 9*(len(n)-1)
else:
    if len(n) == n.count("9"):
        res = 9*len(n)
    else:
        res = 9*(len(n)-1) + 8

print(res)
