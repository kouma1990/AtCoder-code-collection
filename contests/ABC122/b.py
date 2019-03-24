s = input()

def check(s):
    if s=="A" or s=="C" or s=="G" or s=="T":
        return True
    else:
        return False

max_count = 0
for i in range(len(s)):
    count = 0
    for j in range(i,len(s)):
        if check(s[j]):
            count+=1
        else:
            break
    max_count = max(count,max_count)

print(max_count)