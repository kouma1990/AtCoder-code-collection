n, p = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

a = list(map(lambda x:x%2, a))

odd = a.count(1)
even = a.count(0)

#if p==0:
    