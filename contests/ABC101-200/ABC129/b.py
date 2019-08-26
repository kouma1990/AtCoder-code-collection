n = int(input())
w = [int(i) for i in input().split()]

min_num = 10**10
for i in range(n):
    s = abs(sum(w[:i]) - sum(w[i:]))
    if s < min_num:
        min_num = s

print(min_num)