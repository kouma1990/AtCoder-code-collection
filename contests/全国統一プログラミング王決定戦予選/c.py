import sys
input = sys.stdin.readline

n = int(input())
ab = []
for i in range(n):
    a = list(map(int, input().split()))
    ab.append([a[0]+a[1], a[0], a[1]])

ab = sorted(ab, reverse=True)

a = sum(list(map(lambda x: x[1], ab[::2])))
b = sum((list(map(lambda x: x[2], ab[1::2]))))

print(a-b)