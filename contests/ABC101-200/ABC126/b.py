s = input()
test = ["01","02","03","04","05","06","07","08","09","10","11","12"]
a1 = s[:2]
a2 = s[2:]

if a1 in test and a2 in test:
    print("AMBIGUOUS")
elif a1 in test:
    print("MMYY")
elif a2 in test:
    print("YYMM")
else:
    print("NA")