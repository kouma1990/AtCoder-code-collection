n = int(input())
a = [int(i) for i in input().split()]

count=0
while True:
    check = list(map(lambda x:x%2, a))
    if check.count(1) > 0:
        break
    else:
        a = list(map(lambda x:x//2, a))
        count+=1

print(count)