n, m = (int(i) for i in input().split())

a = m//n

for i in range(a):
    x = a-i
    if m % x == 0:
        print(x)
        break