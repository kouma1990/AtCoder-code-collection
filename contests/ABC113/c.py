import sys
input = sys.stdin.readline
 
N, M = (int(i) for i in input().split())
input_list = [[int(i) for i in input().split()] for i in range(M)] 
 
m_list = [[] for j in range(N+1)]
 
for inputs in input_list:
    m_list[inputs[0]].append(inputs[1])
 
for arr in m_list:
    arr.sort()
 
for inputs in input_list:
    num = m_list[inputs[0]].index(inputs[1]) + 1
    print(str(inputs[0]).zfill(6) + str(num).zfill(6))