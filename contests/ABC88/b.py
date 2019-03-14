n = int(input())
a = sorted([int(i) for i in input().split()])[::-1]

print(sum(a[::2]) - sum(a[1::2]))
