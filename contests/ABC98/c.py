n = int(input())
s = input()

score = []
score.append(s[1:].count("E"))

for i in range(1, n):
    diff = -1 if s[i] == "E" else 0
    diff += 1 if s[i-1] == "W" else 0
    score.append(score[-1]+diff)

print(min(score))