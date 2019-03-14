x = int(input())

max_num = 1
for i in range(2, int(x**(1/2)+1) ):
    for j in range(1, 11):
        num = i**j
        if num <= x:
            if num > max_num:
                max_num = num
        else:
            break

print(max_num)