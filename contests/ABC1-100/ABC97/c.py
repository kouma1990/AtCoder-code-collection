import bisect

s = input()
k = int(input())

alpha_list = [chr(i) for i in range(97, 97+26)] #["a","b",...."c"]
dic = []
for i in range(len(s)):
    dic = sorted(dic)
    if k < bisect.bisect_left(dic,s[i]):
        continue
    for j in range(i+1, min(i+6, len(s)+1)):
        s0 = s[i:j]
        
        if s0 not in dic:
            dic.append(s0)

print(sorted(dic)[k-1])