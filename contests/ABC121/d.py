#a, b = (int(i) for i in input().split())  

a = 123
b = 456
diff = b-a+1

a_bin = bin(a)
b_bin = bin(b)
a_bin_num = len(a_bin[2:])
b_bin_num = len(b_bin[2:])
diff_bin_num = len(bin(diff)[2:])


a_bin_pad = "0"*(b_bin_num-a_bin_num) + a_bin[2:]
check_num = [diff] * b_bin_num
modify_num = [0] * b_bin_num
result = ""
for i in range(b_bin_num):
    check_num[i] = diff % (2**(i+1))
    modify_num[i] = (2**(i+1)) - int("0b" + a_bin_pad[-(i+1):], 0)
    
    if i == 0:
        if check_num[i] == 0:
            result = "0"
        else:
            result = a_bin_pad[-(i+1)]
    else:
        print("test")
    #if check_num[i] < modify_num[i]:
        
print(result)

#x = int("0b"+x_bin, 0)


#for i in a_bin_pad[::-1]:
#    print(i)

print(check_num)
print(modify_num)

"""
count_1 = [0]*b_bin_num

for i in range(a,b+1):
    i_bin = bin(i)[2:][::-1]
    for j in range(len(i_bin)):
        if i_bin[j] == "1":
            count_1[j] += 1

print(count_1)
x_bin = ""
for i in count_1[::-1]:
    if i % 2 == 0:
        x_bin += "0"
    else:
        x_bin += "1"

x = int("0b"+x_bin, 0)

print(x)
"""