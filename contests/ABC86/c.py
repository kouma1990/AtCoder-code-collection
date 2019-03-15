n = int(input())
e = [[int(i) for i in input().split()] for i in range(n)]

ct = 0
cx = 0
cy = 0

result = "Yes"
for e_ in e:
    t = e_[0]
    x = e_[1]
    y = e_[2]

    dt = t - ct
    dxy = abs(cx - x) + abs(cy - y)
    if dxy > dt or (dt - dxy)%2 == 1:
        result = "No"
        break

    ct = t
    cx = x
    cy = y

print(result)