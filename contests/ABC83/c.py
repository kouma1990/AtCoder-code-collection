x, y = (int(i) for i in input().split())

count = 1
while True:
    x = x*2
    if x > y:
        break
    count+=1
print(count)