s = input()

for i in range(len(s)):
    tmp = s[:-(i+1)]
    if len(tmp)%2 == 1:
        continue

    c = len(tmp) // 2
    if tmp[:c] == tmp[c:]:
        print(len(tmp))
        exit()
