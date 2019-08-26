n, m = (int(i) for i in input().split())

def f():
    if n*2 > m:
        return m//2
    
    return n + (m-n*2) // 4

print(f())