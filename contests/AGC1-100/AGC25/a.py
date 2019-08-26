n = int(input())

min_num = 10**9
for a in range(1,n):
    b = n-a
    a_s = sum(list(map(lambda x: int(x), str(a))))
    b_s = sum(list(map(lambda x: int(x), str(b))))
    num = a_s+b_s
    min_num = min(num, min_num)

print(min_num)
