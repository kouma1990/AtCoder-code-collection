n = int(input())
l = sorted([int(i) for i in input().split()])
if l[-1] < sum(l-l[-1]):
    print("Yes")
else:
    print("No")