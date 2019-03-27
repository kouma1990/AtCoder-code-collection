s = input()
st = s.index("A")
en = s[::-1].index("Z") 
print(len(s)-en-st)