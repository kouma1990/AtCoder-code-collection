n,k = (int(i) for i in input().split())
s = input()

start = s[0]
arr = []
pre = start
cnt = 0
for x in s:
    if x == pre:
        cnt+=1
        continue
    else:
        pre = x
        arr.append(cnt)
        cnt = 1

arr.append(cnt)

if len(arr) == 1:
    print(arr[0])
    exit()

m = 0
if start == "1":
    now = sum(arr[:2*k+1])
    m = now
    for i in range(1, (len(arr)//2)-k+1):
        now = now - arr[2*i-1] - arr[2*i-2] + sum(arr[2*i+2*k-1:2*i+2*k+1]) 
        m = max(now, m)

else:
    m = sum(arr[:2*k])
    now = sum(arr[1:2*k+2])
    m = max(now, m)
    for i in range(1, ((len(arr)+1)//2)-k):
        now = now - arr[2*i] - arr[2*i-1] + sum(arr[2*i+2*k:2*i+2*k+2])
        m = max(now, m)
    
print(m)
        