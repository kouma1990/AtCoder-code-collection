a = [int(i) for i in input().split()]  

max_a = max(a)
a[a.index(max(a))] = 0

print(max_a*10 + sum(a))