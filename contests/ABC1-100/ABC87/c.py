n = int(input())
a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]

max_score = 0
for i in range(n):
    score = sum(a1[:i+1]) + sum(a2[i:])
    max_score = max(score, max_score)

print(max_score)