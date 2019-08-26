n = int(input())
a = [int(i) for i in input().split()]

mu = round(sum(a)/n)

print(sum(list(map(lambda x:(x-mu)**2,a))))
