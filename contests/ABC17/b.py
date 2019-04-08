s = input()
num = s.count("ch")*2 + s.count("o") + s.count("k") + s.count("u")
if len(s) == num:
    print("YES")
else:
    print("NO")