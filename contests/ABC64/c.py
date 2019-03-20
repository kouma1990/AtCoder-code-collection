n = int(input())
a = [int(i) for i in input().split()]

count = 0
for i in range(8):
    if len(list(filter(lambda x:i*400<=x and x<400*(i+1), a))) > 0:
        count+=1

x = len(list(filter(lambda x:3200<=x, a)))
if count==0:
    count=1
    x-=1

print("{} {}".format(count, count+x))