from math import *
def calc(k):
    return [ int(factorial(k)/(factorial(i)*factorial(k-i)))*2**i for i in range(k+1)]

s = input()

left = {"A":0,"B":0,"C":0,"?":0}
right = {"A":0,"B":0,"C":s.count("C"),"?":s.count("?")} # C, ?の値しか使わない

cnt = 0
for x in s:
    right[x] -= 1
    if x == "?" or x=="B":
        r = right["C"] * (right["?"]*3 if right["?"]>0 else 1)
        l = left["A"] * (left["?"]*3 if left["?"]>0 else 1)
        cnt += r*l
    left[x] += 1

print(cnt)

print(calc(0))
print(calc(1))
print(calc(2))
print(calc(3))
        