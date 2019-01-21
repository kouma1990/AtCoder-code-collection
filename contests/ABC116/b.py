a = int(input())
 
num_list = [a]
init_flag = True
result = 1
while True:
	result += 1
	num = num_list[-1]
	if num%2 == 0:
		new_num = int(num/2)
	else:
		new_num = int(3*num+1)
 
	if not init_flag and new_num in num_list:
		#print(num_list.index(num))
		print(result)
		break
	num_list.append(new_num)
	init_flag = False
	