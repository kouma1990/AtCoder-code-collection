x,y = (int(i) for i in input().split())

if x%y==0:
    print(-1)
    exit()

for i in range(2,(10**18)//x):
    if x*i%y!=0:
        print(x*i)
        exit()

print(-1)