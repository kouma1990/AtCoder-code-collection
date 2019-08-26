x = int(input())

s = 0
for i in range(1, x+1):
    s+=i
    if s >= x:
        print(i)
        break