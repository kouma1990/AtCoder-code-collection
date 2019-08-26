n = int(input())
a = [int(input()) for i in range(5)]
t = 4 if n%min(a) == 0  else 5
print(n//min(a)+t)