n, k = (int(i) for i in input().split())
d = [i for i in input().split()]

for i in range(n,n*100):
    flg=True
    for j in str(i):
        if j in d:
            flg=False
            break;

    if flg:
        print(i)
        break