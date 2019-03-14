a, b, k = (int(i) for i in input().split())

len_ab = b-a+1

if (len_ab+1) // 2 <= k:
    for i in range(a, b+1):
        print(i)

else:
    for i in range(a, a+k):
        print(i)
    for i in range(b-k+1, b+1):
        print(i)