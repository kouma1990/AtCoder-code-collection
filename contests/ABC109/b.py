n = int(input()) 
a = [input() for i in range(n)] 

used = [a[0]]
pre = a[0]
for i in a[1:]:
    if i not in used and pre[-1] == i[0]:
        used.append(i)
        pre = i
    else:
        print("No")
        exit()

print("Yes")