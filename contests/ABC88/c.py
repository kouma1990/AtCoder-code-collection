c = []
c.append([int(i) for i in input().split()])
c.append([int(i) for i in input().split()])
c.append([int(i) for i in input().split()])

for i in range(2):
    a0 = c[i][0] - c[i+1][0]
    a1 = c[i][1] - c[i+1][1]
    a2 = c[i][2] - c[i+1][2]
    if a0 != a1 or a1 != a2:
        print("No")
        exit()

for i in range(2):
    a0 = c[0][i] - c[0][i+1]
    a1 = c[1][i] - c[1][i+1]
    a2 = c[2][i] - c[2][i+1]
    if a0 != a1 or a1 != a2:
        print("No")
        exit()
print("Yes")
