import sys
input = sys.stdin.readline
 
N, M = (int(i) for i in input().split())
py_list = [[int(i) for i in input().split()] + [0] for i in range(M)] 
m_list = [[] for j in range(N+1)]
 
sorted_py_list = sorted(py_list, key=lambda x:x[1])

city_list = {}
for py in sorted_py_list:
    city_list[py[0]] = city_list[py[0]]+1 if py[0] in city_list else 1
    py[2] = city_list[py[0]]
 
for py in py_list:
    print(str(py[0]).zfill(6) + str(py[2]).zfill(6))
