n = int(input())
a = [int(i) for i in input().split()]

b = 0
for x in a:
    b += 1/x

print(1/b)