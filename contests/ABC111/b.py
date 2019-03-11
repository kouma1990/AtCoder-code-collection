n = int(input())

for i in range(1, 10):
    if n <= 111*i:
        print(111*i)
        exit()