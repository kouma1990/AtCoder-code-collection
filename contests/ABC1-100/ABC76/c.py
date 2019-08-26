s = input()
t = input()
s_list = list(s)

for i in range(len(s)-len(t)+1):
    flg = True
    for j in range(len(t)):
        if not (s[-len(t)-i+j] == "?" or s[-len(t)-i+j] == t[j]):
            flg = False
            break
    
    if flg:
        for j in range(len(t)):
            s_list[-len(t)-i+j] = t[j]
        
        s = "".join(s_list)
        s = s.replace("?", "a")

if s.count("?") > 0:
    print("UNRESTORABLE")
else:
    print(s)
