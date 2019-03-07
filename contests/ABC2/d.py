import re

n, m = (int(i) for i in input().split())  
e = [[int(i)-1 for i in input().split()] for i in range(m)] 

def state2indexarr(state):
    arr = []
    for i in range(n):
        if int(state[i]) == 1:
            arr.append(i)
    return arr
        

def check(index, state):
    l = state2indexarr(state)
    for index_2 in l:
        index_2 = int(index_2)
        flg = False
        for x in e:
            if (x[0] == min(int(index_2),int(index))) and (x[1] == max(int(index_2),int(index))):
                flg = True
                break
        
        if not flg:
            return False
    
    return True

def output(index, state):
    if index == n:
        return state.count("1")

    ret0 = output(index+1, state)
    if check(index, state):
        ret1 = output(index+1, state[:index] + "1" + state[(index+1):])
    else:
        return max(ret0, state.count("1"))

    return max(ret0, ret1)

print(output(0, "0"*n))