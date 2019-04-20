n = int(input())
a = [int(input()) for i in range(n)]

sum_num = sum(a)

l = [0]
l2 = [0]
cnt = 0
for x in a:
    c = []
    c2 = []
    for idx, l_ in enumerate(l): 
        if l_+x < sum_num/2:
            c.append(l_+x)
            c2.append(l2[idx]+1)
            cnt += 2**(n-(l2[idx]+1)) -1 

    l += c
    l2 += c2

print(l)
print(cnt)

