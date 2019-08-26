n = int(input())
a = [int(input())-1 for i in range(n)]

used = [0]*n
current = 0
count = 0
while True:
    if used[current] == 1:
        print(-1)
        exit()
    used[current] = 1
    current = a[current]
    count += 1
    

    if current == 1:
        print(count)
        break