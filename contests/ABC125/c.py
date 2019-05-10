n = int(input())
a = [int(i) for i in input().split()]

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

dic = {}
for i, x in enumerate(a):
    if i <2:
        for y in make_divisors(x):
            if y in dic:
                dic[y] += 1
            else:
                dic[y] = 1
    else:
        l = make_divisors(x)
        for k,v in dic.items():
            if k in l:
                dic[k]+=1

        dic = {k:v for k,v in dic.items() if v>i-1}
        
for k,v in sorted(dic.items(), reverse=True):
    print(k)
    exit()