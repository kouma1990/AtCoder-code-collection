from fractions import gcd

def pollard_rho(n):
    x, y, d = 2, 2, 1

    while d == 1:
        x = (x*x + 1) % n
        y = (y*y + 1) % n
        y = (y*y + 1) % n
        d = gcd(abs(x-y), n)

    if d != n:
        return d