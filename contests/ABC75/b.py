h, w = (int(i) for i in input().split())
s = [input() for i in range(h)]

result = []
for j in range(h):
    r = ""
    for i in range(w):
        if s[j][i] == "#":
            r += "#"
            continue

        si = 0 if i == 0 else i-1
        sj = 0 if j == 0 else j-1
        ei = w if i == w-1 else i+2
        ej = h if j == h-1 else j+2
        count = 0
        for j_ in range(sj,ej):
            for i_ in range(si,ei):
                if s[j_][i_] == "#":
                    count += 1
        r += str(count)
    result.append(r)

for j in range(h):
    print(result[j])

