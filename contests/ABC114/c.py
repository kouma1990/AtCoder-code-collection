n = int(input())

import bisect
l = []
def dfs(num, index):
    if index == 9:
        if (num.find("3") != -1) and (num.find("5") != -1) and (num.find("7") != -1):
            l.append(int(num))
        return 0
        
    if num == "":
        ret0 = dfs(num + "" , index+1)
    ret1 = dfs(num + "3", index+1)
    ret2 = dfs(num + "5", index+1)
    ret3 = dfs(num + "7", index+1)

    return 0

dfs("", 0)

print (bisect.bisect_right(l,n))