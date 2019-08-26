n, m = (int(i) for i in input().split())  
e = [[int(i) for i in input().split()] for i in range(n)] 

count_list = []
for x in e:
    count_list += x[1:]

result = 0
for i in range(m):
    if count_list.count(i+1) == n:
        result += 1

print(result)
