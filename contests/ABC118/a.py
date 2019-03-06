a, b = (int(i) for i in input().split()) 
print(a+b if b%a == 0 else b-a)
