n = int(input())
s = input()

right_white = s.count(".")
left_black = 0

min_num = min(right_white, n-right_white)

for x in s:
    if x == ".":
        right_white -= 1
    else:
        left_black += 1

    min_num = min(min_num, right_white+left_black)

print(min_num)
