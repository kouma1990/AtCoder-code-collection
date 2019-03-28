s = input()

res = int(s)
for i in range(1,len(s)):
    l = len(s)-i
    for j in range(len(s)-l+1):
        x = i-1
        if j>0 and j<len(s)-l:
            x -=1
        res+=int(s[j:j+l])*(2**x)

print(res)
