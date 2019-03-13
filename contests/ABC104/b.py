s = input()

if s[0] != "A":
    print("WA")
    exit()

if s[1].isupper() or s[-1].isupper():
    print("WA")
    exit()

count = 0
for s_ in s[2:]:
    if s_.isupper():
        if s_ == "C":
            count += 1
        else:
            print("WA")
            exit()
        

if count == 1:
    print("AC")
else:
    print("WA")