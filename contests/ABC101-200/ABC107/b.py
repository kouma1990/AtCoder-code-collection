H, W = (int(i) for i in input().split())
e = [input() for i in range(H)] 

new_e = []
for row in e:
    if row.count("#") > 0:
        new_e.append(row)

use_col = []
for row in new_e:
    for col in range(W):
        if row[col] == "#" and col not in use_col:
            use_col.append(col)
            
for row in new_e:
    x=""
    for col in sorted(use_col):
        x += row[col]
    print(x)

