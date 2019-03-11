n = int(input())
v = [int(i) for i in input().split()]

from collections import Counter

v_0 = v[0::2]
v_1 = v[1::2]
v_0_ = Counter(v_0)
v_1_ = Counter(v_1)
v_0_[-1] = 0
v_1_[-1] = 0
v_0_ = v_0_.most_common()
v_1_ = v_1_.most_common()

if v_0_[0][0] != v_1_[0][0]:
    print(n-v_0_[0][1]-v_1_[0][1])
else:
    if v_0_[0][1] + v_1_[1][1] > v_0_[1][1] + v_1_[0][1]:
        print(n - v_0_[0][1] - v_1_[1][1])
    else:
        print(n - v_0_[1][1] - v_1_[0][1])
