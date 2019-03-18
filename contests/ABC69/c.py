n = int(input())
a = [int(i) for i in input().split()]

a2 = len(list(filter(lambda x:x%2==0, a)))
a4 = len(list(filter(lambda x:x%4==0, a)))

if n == a2:
    print("Yes")
    exit()

a2_ = a2 - a4
n = n if a2_==0 else (n-a2_+1)
if n//2 <= a4:
    print("Yes")
else:
    print("No")
