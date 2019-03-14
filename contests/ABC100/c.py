n = int(input())
a = [int(i) for i in input().split()]

count = 0
while True:
    flg = True
    for i in range(n):
        if a[i] % 2 == 0:
            count+=1
            a[i] = a[i] / 2
            flg=False
    
    if flg:
        print(count)
        break