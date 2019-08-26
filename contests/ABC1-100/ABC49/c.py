s = input()

# dream dreamer erase eraser
def f():
    global s
    while True:
        if len(s) <= 9:
            if s in ["dream","dreamer","erase","eraser"]:
                return "YES"
            else:
                return "NO"

        if s[:5] == "dream":
            if s[5:7] == "er" and s[7] != "a":
                s = s[7:]
            else:
                s = s[5:]
        elif s[:5] == "erase":
            if s[5] == "r":
                s = s[6:]
            else:
                s = s[5:]
        else:
            return "NO"
            

print(f())