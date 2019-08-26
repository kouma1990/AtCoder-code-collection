import sys
input = sys.stdin.readline
n,m = (int(i) for i in input().split())
ab = [[int(i)-1 for i in input().split()] for i in range(m)]

ab = list(filter(lambda x:x[0]==0 or x[1]==n-1, ab))
ab0 = list(filter(lambda x:x[0]==0,ab))
abn = list(filter(lambda x:x[1]==n-1,ab))

ab0_bin = ["0"]*n
abn_bin = ["0"]*n
for x in ab0:
    ab0_bin[x[1]] = "1"
for x in abn:
    abn_bin[x[0]] = "1"

ab0_bin = "".join(ab0_bin)
abn_bin = "".join(abn_bin)

if bin(int(ab0_bin,2) & int(abn_bin, 2))[2:].count("1") > 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
