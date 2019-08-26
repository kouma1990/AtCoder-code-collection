s = input()

b = []
for x in s:
    if x in b:
        print("no")
        exit()
    b.append(x)

print("yes")
