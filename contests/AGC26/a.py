n = int(input())
a = [int(i) for i in input().split()]

l = []
pre = ""
cnt = 0
for x in a:
    if pre == x:
        cnt += 1
    else:
        l.append(cnt)
        cnt = 1
        pre = x

l.append(cnt)
l = l[1:]

print( sum(list(map(lambda x: x//2, l))) )