S = input()
T = input()

def f(S):
    idx = []
    dic = []
    for s in S:
        if s in dic:
            idx.append(dic.index(s))
        else:
            idx.append(len(dic))
            dic.append(s)
    
    return idx

s_idx = f(S)
t_idx = f(T)
for i in range(len(S)):
    if s_idx[i] != t_idx[i]:
        print("No")
        exit()

print("Yes")