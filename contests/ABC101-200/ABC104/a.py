r = int(input())

res = ""
if r < 1200:
    res="ABC"
elif r < 2800:
    res="ARC"
else:
    res="AGC"
print(res)