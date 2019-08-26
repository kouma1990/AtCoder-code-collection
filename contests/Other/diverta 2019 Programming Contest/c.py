n = int(input())
s = [input() for i in range(n)]

b = 0
a = 0
ba = 0

cnt = 0
for x in s:
    if x[0] == "B" and x[-1] == "A":
        ba+=1
    if x[0] == "B":
        b+=1
    if x[-1] == "A":
        a+=1
    cnt += x.count("AB")

cnt2 = 0
if ba==b and ba==a and ba!=0:
    cnt2 = ba-1
else:
    cnt2 = min(a,b)

print(cnt+cnt2)