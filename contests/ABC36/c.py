n = int(input())
a = [int(input()) for i in range(n)]

dic = {}
for i,x in enumerate(sorted(list(set(a)))):
    dic[x] = i

for x in a:
    print(dic[x])