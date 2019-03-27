sx, sy, tx, ty = (int(i) for i in input().split())
w = tx-sx
h = ty-sy

res = "U"*h+"R"*w+"D"*h+"L"*(w+1)+"U"*(h+1)+"R"*(w+1)+"DR"+"D"*(h+1)+"L"*(w+1)+"U"
print(res)