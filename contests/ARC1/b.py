a, b　= (int(i) for i in input().split())  

count = 0

while True:
    if a == b:
        break

    c = [a-10, a-5, a-1, a+1, a+5, a+10]
    min_num = 10000000
    for x in c:
        if min_num > abs(b-x):
            min_num = abs(b-x)
            a = x
    count += 1

print(count)