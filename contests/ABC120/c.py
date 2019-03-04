a = input()
 
cnt0 = a.count("0")
cnt1 = a.count("1")
 
print(str(min(cnt0,cnt1)*2))