n = int(input())

h = n//3600
n_ = n%3600
m = n_//60
s = n_%60

h = ("0"+str(h))[-2:]
m = ("0"+str(m))[-2:]
s = ("0"+str(s))[-2:]

print("{}:{}:{}".format(h,m,s))