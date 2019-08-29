s = input()

for x in s:
    if s.count(x) != 2:
        print("No")
        exit()

print("Yes")