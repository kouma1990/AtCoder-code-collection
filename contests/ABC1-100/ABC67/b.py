n,k = (int(i) for i in input().split())
a = sorted([int(i) for i in input().split()], reverse=True)

print(sum(a[:k]))