n = int(input())
a = [int(i) for i in input().split()]

num = 0
for x in a:
    y = x
    while True:
        if y == 1:
            break

        if y%2==0 or (y-2)%3==0:
            y-=1
            num+=1
        else:
            break

print(num)
        