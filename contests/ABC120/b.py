a, b, k = (int(i) for i in input().split())
 
num_list = []
for i in range(min(a,b)):
    if a%(i+1) == 0 and b%(i+1) == 0:
        num_list.append(i+1)
 
print(num_list[-k])