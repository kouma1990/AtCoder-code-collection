s = input()
t = input()

s_ = sorted(s)
t_ = sorted(t)[::-1]

s_ = "".join(s_)
t_ = "".join(t_)

if s_ < t_:
    print("Yes")
else:
    print("No")