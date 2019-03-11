n, m, X, Y = (int(i) for i in input().split())
x = [int(i) for i in input().split()]  
y = [int(i) for i in input().split()] 

x_max = max(X, max(x))
Z = x_max + 1

if Y < Z or min(y) < Z:
    print("War")
else:
    print("No War")