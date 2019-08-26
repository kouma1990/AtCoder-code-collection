n = int(input())
e = [[int(i) for i in input().split()] for i in range(n)]

count = 0
for x in e:
    count += x[1]-x[0]+1
print(count)