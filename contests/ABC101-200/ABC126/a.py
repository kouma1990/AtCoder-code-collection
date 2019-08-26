n, k = (int(i) for i in input().split())
s = input()
k = k-1
print(s[:k] + s[k].lower() + s[k+1:])