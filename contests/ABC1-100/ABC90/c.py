n, m = (int(i) for i in input().split())

def f():
    if n == 1 and m == 1:
        return 1
    if n == 1 or m == 1:
        return max(n,m)-2
    return n*m - 2*n - 2*m + 4

print(f())