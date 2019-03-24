# 高速版input
import sys
input = sys.stdin.readline

n, q = (int(i) for i in input().split())
s = input()

mem = [0]
count = 0
for i in range(1, len(s)):
    if s[i-1]+s[i] == "AC":
        count +=1
    mem.append(count)
    
for x in [[int(i)-1 for i in input().split()] for i in range(q)]:
    res = mem[x[1]] - mem[x[0]]
    print(res)
