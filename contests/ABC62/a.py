x,y = (int(i) for i in input().split())

a = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
for b in a:
    if x in b and y in b:
        print("Yes")
        exit()
print("No")