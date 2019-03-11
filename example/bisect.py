# 二分探索
import bisect

A = [0,1,2,3,5,6,7]
b = 4
bisect.bisect_left(A,b) # 3
b = 5
bisect.bisect_left(A,b) # 3
bisect.bisect_right(A,b) # 4