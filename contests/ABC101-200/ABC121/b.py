N, M, C = (int(i) for i in input().split())  
B = [int(i) for i in input().split()]
a_list  = [[int(i) for i in input().split()] for i in range(N)] 

count = 0
for A in a_list:
    sum_num = 0
    for i in range(M):
        sum_num += A[i] * B[i] 

    if sum_num + C > 0:
        count += 1

print( count )
