# 途中 WA
n = 3
k = 7
a = [1, 6, 3]

n = 4
k = 9
a = [7,4,0,3]

n = 1
k = 0
a = [1000000000000]
k_bins = len(bin(k))-2
count_0 = [0]*k_bins
count_1 = [0]*k_bins
for a_ in a:
    a_bin = bin(a_)
    a_bins = len(a_bin) - 2
    for i in range(k_bins):
        if (i+1 > a_bins) or (a_bin[-i-1] == '0'):
            count_0[i] += 1
        else:
            count_1[i] += 1

#x_bin = ""
res = 0
for i in range(k_bins):
    res += max(count_0[i], count_1[i])*2**i
    
print(res)

"""
x = int("0b"+x_bin, 0)
result = 0
for a_ in a:
    result += a_ ^ x
print(result)

"""