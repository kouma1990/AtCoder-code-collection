n = int(input())
a = sorted([int(i) for i in input().split()])

def f():
    global a
    cnt = 1 + (n%2)
    if n%2 == 1:
        if a[0] != 0:
            return 0
        a = a[1:]

    # check
    for i in range(len(a)):
        if a[i] != cnt:
            return 0

        if i%2 == 1:
            cnt+=2

    return 2**(n//2)

print(f()%(10**9+7))

