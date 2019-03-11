n = input()

result = ""
for i in n:
    result += "1" if i == "9" else "9"

print(result)