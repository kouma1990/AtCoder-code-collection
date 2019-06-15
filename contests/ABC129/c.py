n, m = (int(i) for i in input().split())
a = [int(input()) for i in range(m)]

def Fib(n1):
    a1, b1 = 0, 1
    if n1 == 1:
        return a1
    elif n1 == 2:
        return b1
    else:
        for i in range(n1-2):
            a1, b1 = b1, a1 + b1
        return b1

l = []
pre = -1
for x in a:
    if x-pre == 1:
        print(0)
        exit()
    l.append(Fib(x-pre-1 +1))
    pre = x

l.append(Fib(n-pre +1))

res = 1
for x in l:
    res *= x

print(res % 1000000007)