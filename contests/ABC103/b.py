s = input()
t = input()

def f():
    if s==t:
        return "Yes"
    for i in range(1, len(t)):
        if (s[-i:] + s[:-i]) == t:
            return "Yes"
    return "No"

print(f())