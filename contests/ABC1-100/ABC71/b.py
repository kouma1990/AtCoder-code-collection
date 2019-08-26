s = input()

for i in [chr(i) for i in range(97, 97+26)]:
    if s.count(i) == 0:
        print(i)
        exit()

print("None")
