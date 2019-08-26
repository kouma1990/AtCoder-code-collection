n = int(input())
e = [[i for i in input().split()] for i in range(n)] 

result = 0
for x in e:
    if x[1] == "JPY":
        result += float(x[0])
    else:
        result += float(float(x[0])*380000)

print(result)