a,b,c,k = (int(i) for i in input().split())
s,t = (int(i) for i in input().split())

res = s*a + t*b
print(res if s+t<k else res-(c*(s+t)))