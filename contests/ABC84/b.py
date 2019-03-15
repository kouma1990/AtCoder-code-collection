a, b = (int(i) for i in input().split())
s = input()

def f():
    if s.count("-") != 1:
        return "No"
    x = s.split("-")
    
    if len(x[0]) == a and len(x[1]) == b:
        return "Yes"
    return "No"

print(f())