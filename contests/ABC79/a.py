n = input()

for i in range(10):
    s = str(i)*3
    if n.count(s) > 0:
        print("Yes")
        exit()
print("No") 