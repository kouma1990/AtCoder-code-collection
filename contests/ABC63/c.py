n = int(input())
a = [int(input()) for i in range(n)]

res = sum(a)
if res%10 !=0:
    print(res)
    exit()

b = sorted(list(filter(lambda x:x%10!=0, a)))
if len(b) == 0:
    print(0)
    exit()
print(res-b[0])
