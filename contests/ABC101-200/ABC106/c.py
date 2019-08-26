s = input()
k = int(input())

result = "1"
for i in range( min(len(s),k) ):
    if s[i] != "1":
        result = s[i]
        break
        
print(result)