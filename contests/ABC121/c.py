N, M = (int(i) for i in input().split())  
e = sorted([[int(i) for i in input().split()] for i in range(N)])

result = 0
for x in e:
    if M > x[1]:
        M -= x[1]
        result += x[0] * x[1]
    else:
        result += x[0] * M
        break

print(result)


