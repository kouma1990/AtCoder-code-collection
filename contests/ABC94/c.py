n = int(input())
X = [int(i) for i in input().split()]
X_s = sorted(X)

x1 = X_s[(n//2)-1]
x2 = X_s[n//2]

for x in X:
    if x <= x1:
        print(x2)
    else:
        print(x1)
        

