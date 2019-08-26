a, b = (int(i) for i in input().split())

if a==b:
    print("Draw")
elif a==1:
    print("Alice")
elif b==1:
    print("Bob")
elif max(a,b) == a:
    print("Alice")
else:
    print("Bob")