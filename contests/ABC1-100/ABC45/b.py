cards = [input() for i in range(3)]

now = 0
index =[0,0,0]
dic={"a":0,"b":1,"c":2}

while True:
    if index[now] == len(cards[now]):
        break
    idx = index[now]
    index[now] += 1
    now = dic[cards[now][idx]]
    

print("ABC"[now])