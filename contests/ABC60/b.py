a,b,c = (int(i) for i in input().split())
for i in range(1,b):
    if a*i%b == c:
        print("YES")
        exit()
    
print("NO")