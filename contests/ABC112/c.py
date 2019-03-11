n = int(input())
e = sorted([[int(i) for i in input().split()] for i in range(n)], key=lambda x:x[2])[::-1]

def f():
    for x in range(101):
        for y in range(101):
            flg = True
            H = e[0][2] + abs(x-e[0][0]) + abs(y-e[0][1])
            for e_ in e:
                if (e_[2] == 0):
                    if H > abs(x-e_[0]) + abs(y-e_[1]):
                        flg = False
                        break
                    else:
                        continue
                
                if H != e_[2] + abs(x-e_[0]) + abs(y-e_[1]):
                    flg = False
                    break
            if flg:
                return (x, y, H)
result = f()
print("{} {} {}".format(result[0], result[1], result[2]) )