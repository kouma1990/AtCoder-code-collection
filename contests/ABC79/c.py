s = input()
a, b, c, d = (int(s[0]),int(s[1]),int(s[2]),int(s[3]))

def f(idx):
    return "+" if idx==0 else "-"
for i in range(2):
    for j in range(2):
        for k in range(2):
            num = a
            num += b if i == 0 else -b
            num += c if j == 0 else -c
            num += d if k == 0 else -d

            if num == 7:
                result = str(a) + f(i) + str(b) + f(j) + str(c) + f(k) + str(d) + "=7"
                print(result)
                exit() 