n = int(input())

for i in range(26):
    for j in range(16):
        sum_num = 4*i + 7*j
        if 100 < sum_num:
            break

        if sum_num == n:
            print("Yes")
            exit()
print("No")