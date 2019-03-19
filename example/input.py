# 高速版input
import sys
input = sys.stdin.readline

# 1行に1つの数字
a = int(input())

# 1行に複数の数字：　1 3 5 7
# a=1, b=3, c=5, d=7
a, b, c, d = (int(i) for i in input().split())
# a=[1,3,5,7]
a = [int(i) for i in input().split()]

# 複数行の数字をリスト
n = int(input())
a = [int(input()) for i in range(n)]

# 複数行に複数の数字
n = int(input())
e = [[int(i) for i in input().split()] for i in range(n)]