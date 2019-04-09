n = int(input())
ans = 2025-n

for i in range(1,10):
    if ans%i == 0:
        x = ans//i
        if len(str(x)) == 1:
            print("{} x {}".format(i, x))