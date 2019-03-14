n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

max_score = 0
for s_ in s:
    score = s.count(s_) - t.count(s_)
    if score > max_score:
        max_score = score

print(max_score)