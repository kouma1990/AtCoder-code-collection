s = input()
pre = s[0]
for x in s[1:]:
    if x == pre:
        print("Bad")
        exit()

    pre = x

print("Good")
